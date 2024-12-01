from app.schemas.base import BaseSchema
from pydantic import BaseModel


class Resource2Schema(BaseSchema):
    id: int | None
    attr1: str
    attr2: int


class Resource2CreationRequestSchema(BaseSchema):
    attr1: str
    attr2: int


class Resource2CreationResponseSchema(BaseSchema):
    data: Resource2Schema
