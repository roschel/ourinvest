from typing import List

from pydantic import BaseModel, Field


class OperationsIn(BaseModel):
    type: str = Field(description="Se a operação é de envio(OUT) ou de recebimento(IN)")
    spot: float = Field(description="valor da moeda no mercado")
    spread: float = Field(description="valor do percentual")
    fx_quantity: float = Field(description="quantidade de moeda estrangeira sendo negociada")
    created_at: str = Field(description="horário da execução da operação em UTC escrita segundo ISO 8601")


class OperationsOut(BaseModel):
    real_quantity: float = Field()
    created_at: str = Field(description="horário da execução da operação em UTC escrita segundo ISO 8601")


class ClientInfo(BaseModel):
    balance: float = Field(description="saldo em reais do cliente")
    limit: float = Field(description="limite em reais do quanto o cliente pode operar em um período")


class DocIn(BaseModel):
    balance: float = Field(description="saldo em reais do cliente")
    limit: float = Field(description="limite em reais do quanto o cliente pode operar em um período")
    operations: List[OperationsIn] = Field(description="operações realizadas")


class DocOut(BaseModel):
    client_info: ClientInfo = Field()
    operations: List[OperationsOut] = Field()
