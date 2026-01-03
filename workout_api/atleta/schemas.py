from typing import Annotated, Optional
from pydantic import PositiveFloat, Field


from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta


## Esse mapeamento é para definir os dados do atleta com o esqueam do banco de dados
class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="Juju", max_length=50)
    ]

    cpf: Annotated[
        str, Field(description="CPF do atleta", example="12345678902", max_lenght=11)
    ]

    idade: Annotated[int, Field(description="Idade do atleta", example=24)]

    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=70.5)]

    altura: Annotated[
        PositiveFloat, Field(description="Altura do atleta", example=1.45)
    ]

    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_lenght=1)]

    categoria: Annotated[CategoriaIn, Field(descripton="Categoria do atleta")]

    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


# Esquema para atualizar um usuário por nome e idade
class AtletaUpdate(BaseSchema):
    nome: Annotated[
        Optional[str],
        Field(None, description="Nome do atleta", example="Joao", max_length=50),
    ]
    idade: Annotated[
        Optional[int], Field(None, description="Idade do atleta", example=20)
    ]


# Retorno


class AtletaInfor(BaseSchema):

    nome: Annotated[
        Optional[str],
        Field(None, description="Nome do atleta", example="Joao", max_length=50),
    ]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]
    categoria: Annotated[CategoriaIn, Field(descripton="Categoria do atleta")]
