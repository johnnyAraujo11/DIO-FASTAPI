from typing import Annotated
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema
from pydantic import UUID4


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Bom de Bola",
            max_lenght=20,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Endereco do centro de treinamento",
            example="Rua 123",
            max_lenght=30,
        ),
    ]
    proprietario: Annotated[
        str, Field(description="Nome do proprietario", example="Joao", max_lenght=50)
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento", example="FitAll", max_lenght=20
        ),
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]
