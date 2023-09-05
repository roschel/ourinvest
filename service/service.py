from model.models import DocIn, OperationsOut, DocOut, ClientInfo, OperationsIn


class PeopleService:
    def __init__(self, document: DocIn):
        self.document = document
        self.operations_out = []

    def calculate(self):
        for operation in self.document.operations:
            if operation.type.lower() == "in":
                self._calculate_in(operation)
            else:
                self._calculate_out(operation)

        client_info = ClientInfo(**self.document.model_dump())
        result = DocOut(client_info=client_info, operations=self.operations_out)

        self._save_as_file(result)
        return result

    def _calculate_in(self, operation: OperationsIn):
        operation_result = operation.fx_quantity * (1 - operation.spread) * operation.spot
        if self._validate_limit_rules(operation_result):
            self.document.balance += operation_result
            self.document.limit -= operation_result
            self.operations_out.append(
                OperationsOut(
                    real_quantity=operation_result,
                    created_at=operation.created_at
                )
            )

    def _calculate_out(self, operation: OperationsIn):
        operation_result = operation.fx_quantity * (1 + operation.spread) * operation.spot
        if self._validate_limit_rules(operation_result):
            self.document.balance -= operation_result
            self.document.limit -= operation_result
            self.operations_out.append(
                OperationsOut(
                    real_quantity=operation_result * -1 if operation_result > 0 else operation_result,
                    created_at=operation.created_at
                )
            )

    def _validate_limit_rules(self, operation_result: float) -> bool:
        rules = [
            self.document.limit > 0,
            self.document.limit >= operation_result
        ]
        return all(rules)

    def _save_as_file(self, result):
        with open('data/output.json', 'w') as file:
            file.write(result.model_dump_json())
