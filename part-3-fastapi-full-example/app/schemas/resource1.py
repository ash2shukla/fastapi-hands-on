from app.schemas.base import BaseSchema
from pydantic import BaseModel


class Resource1Schema(BaseSchema):
    id: int
    attr1: str
    attr2: int


class Resource1CreationRequestSchema(BaseSchema):
    attr1: str
    attr2: int


class Resource1CreationResponseSchema(BaseSchema):
    data: Resource1Schema
