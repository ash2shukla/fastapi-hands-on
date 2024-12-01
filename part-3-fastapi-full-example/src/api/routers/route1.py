# subroute 1
from fastapi import APIRouter
from models import resource1
from schemas.resource1 import (
    Resource1CreationRequestSchema,
    Resource1CreationResponseSchema,
)

router = APIRouter(prefix="/route1")


@router.get("")
async def route1_root():
    return "route1 root"


@router.post("/resource1")
async def create_resource1(
    create_req: Resource1CreationRequestSchema,
) -> Resource1CreationResponseSchema:
    print(create_req)
    new_resource = await resource1.create(
        attr1=create_req.attr1, attr2=create_req.attr2
    )
    return Resource1CreationResponseSchema(data=new_resource)
