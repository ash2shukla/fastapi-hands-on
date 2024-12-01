# 1. keep a root router
# 2. and mount rest of the subroutes on this
from app.api.auth import get_current_user
from app.api.routers.resource1 import router as r1_router
from app.api.routers.resource2 import router as r2_router
from app.api.routers.token import router as token_router
from fastapi import APIRouter, Depends

router = APIRouter(prefix="")


router.include_router(r1_router)
router.include_router(r2_router, dependencies=[Depends(get_current_user)])
router.include_router(token_router)
