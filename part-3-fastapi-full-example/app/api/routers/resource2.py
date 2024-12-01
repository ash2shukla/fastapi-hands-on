# subroute 2
from app.common.db import create_session
from app.models import resource2
from app.schemas.resource2 import (
    Resource2CreationRequestSchema,
    Resource2CreationResponseSchema,
)
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/resource2")


@router.post("")
async def resource2_create(
    create_req: Resource2CreationRequestSchema,
    session: AsyncSession = Depends(create_session),
) -> Resource2CreationResponseSchema:
    new_resource2 = await resource2.create(session, **create_req.model_dump())
    # although it works it will show an error on static type checking
    # to remove this error we may use type ignore or typing.cast or just do Resource2Schema.model_validate(new_resource2)
    # before assigning to data
    # thats where sqlmodel comes into the picture
    return Resource2CreationResponseSchema(data=new_resource2)


@router.get("/{id}")
async def resource2_get(
    id: int, session: AsyncSession = Depends(create_session)
) -> Resource2CreationResponseSchema:
    res = await resource2.get(session, id=id)
    return Resource2CreationResponseSchema(data=res)
