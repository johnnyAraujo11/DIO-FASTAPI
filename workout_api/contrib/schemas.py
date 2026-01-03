from pydantic import Field
from typing import Annotated
from pydantic import BaseModel, UUID4
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutMixin(BaseModel):
    id: Annotated[
        UUID4,
        Field(
            description="ID do atleta", example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
        ),
    ]
    created_at: Annotated[datetime, Field("Data de criação")]
