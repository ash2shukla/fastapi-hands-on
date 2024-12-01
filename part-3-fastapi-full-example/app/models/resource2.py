from app.common.settings import settings
from app.models.base import ORMBase

# class Resource2ORM(ORMBase):
#     __tablename__ = "resource2"
#     # use mapping API of sqlalchemy if you are using sqlalchemy 2.0
#     id: Mapped[int] = mapped_column(primary_key=True)
#     attr1: Mapped[str] = mapped_column()
#     attr2: Mapped[int] = mapped_column()
from app.schemas.resource2 import Resource2Schema
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from sqlmodel import Field, SQLModel


class Resource2ORM(SQLModel, Resource2Schema, table=True):
    __tablename__: str = "resource2"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)


async def create(session: AsyncSession, attr1: str, attr2: int) -> Resource2ORM:
    stmt = insert(Resource2ORM).values(attr1=attr1, attr2=attr2).returning(Resource2ORM)
    res = await session.execute(stmt)
    return res.scalar_one()


async def get(session: AsyncSession, id: int) -> Resource2ORM:
    stmt = select(Resource2ORM).where(Resource2ORM.id == id)
    res = await session.execute(stmt)
    return res.scalar_one()
