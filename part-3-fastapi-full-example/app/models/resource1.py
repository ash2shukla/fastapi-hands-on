from app.schemas.resource1 import Resource1Schema


async def create(attr1: str, attr2: int):
    return Resource1Schema(
        id=1,
        attr1=attr1,
        attr2=attr2,
    )
