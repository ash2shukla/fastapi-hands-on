from schemas.resource1 import Resource1


async def create(attr1: int, attr2: str):
    return Resource1(
        id=1,
        attr1=attr1,
        attr2=attr2,
    )
