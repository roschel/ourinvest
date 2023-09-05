from model.models import DocIn, DocOut
from service.service import PeopleService


class TestPeopleService:
    def test_calculate_operation(self, input_json, mocker):
        # GIVEN
        mocker.patch('service.service.PeopleService._save_as_file', return_value=True)
        input_file = DocIn(**input_json)

        # WHEN
        result = PeopleService(input_file).calculate()

        # THEN
        assert isinstance(result, DocOut)
        assert result.client_info.balance == 10000
        assert result.client_info.limit == 0
