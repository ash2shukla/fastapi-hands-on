# subroute 1
from app.models import resource1
from app.schemas.resource1 import (
    Resource1CreationRequestSchema,
    Resource1CreationResponseSchema,
)
from fastapi import APIRouter

router = APIRouter(prefix="/resource1")


@router.get("")
async def resource1_get():
    return "resource1 get"


@router.post("")
async def create_resource1(
    create_req: Resource1CreationRequestSchema,
) -> Resource1CreationResponseSchema:
    print(create_req)
    new_resource = await resource1.create(
        attr1=create_req.attr1, attr2=create_req.attr2
    )
    return Resource1CreationResponseSchema(data=new_resource)
