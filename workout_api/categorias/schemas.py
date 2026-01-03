from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    name: Annotated[
        str, Field(description="Nome da categoria", example="Scale", max_lenght=50)
    ]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="ID da categoria")]
