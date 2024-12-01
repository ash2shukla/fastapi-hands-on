from pydantic import BaseModel


class Resource1(BaseModel):
    id: int
    attr1: int
    attr2: str


class Resource1CreationRequestSchema(BaseModel):
    attr1: int
    attr2: str


class Resource1CreationResponseSchema(BaseModel):
    data: Resource1
