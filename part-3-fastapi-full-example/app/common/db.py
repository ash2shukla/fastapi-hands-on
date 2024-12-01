import contextlib

from app.common.settings import settings
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# 1. create engine
ENGINE = create_async_engine(str(settings.DB_DSN))

# 2. create session maker
session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(ENGINE)


# 3. create a context manager that uses the session maker to manage lifecycle of created session
async def create_session():
    session = session_maker()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
