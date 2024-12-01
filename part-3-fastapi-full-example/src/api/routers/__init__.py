# 1. keep a root router
# 2. and mount rest of the subroutes on this
from fastapi import APIRouter

from .route1 import router as route1_router
from .route2 import router as route2_router

router = APIRouter(prefix="")


router.include_router(route1_router)
router.include_router(route2_router)
