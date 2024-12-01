# subroute 2
from fastapi import APIRouter

router = APIRouter(prefix="/route2")


@router.get("")
async def route2_root():
    return "route2 root"
