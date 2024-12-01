from contextlib import asynccontextmanager

import sqlalchemy.exc
from app.api.middlewares import record_time
from app.api.routers import router as root_router
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware


def register_exc_handlers(app: FastAPI):
    @app.exception_handler(sqlalchemy.exc.NoResultFound)
    def raise_for_notfound(request: Request, exc: sqlalchemy.exc.NoResultFound):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# this is app factory
def create_app():
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        print("Before startup of app")
        yield
        print("Before shutdown of app")

    # register some startup and shutdown events
    app = FastAPI(lifespan=lifespan)

    # include some routers
    app.include_router(root_router)

    # add some state
    app.state.something = "Some global state variables can be given here"
    # ( should ideally be avoided in favour of dependencies )
    # if we want to access it in router we can do it using Request object ie. request.app.state.something

    # or register middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.middleware("http")(record_time)

    # or register exception handlers
    register_exc_handlers(app)

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.api.main:create_app", factory=True, reload=True)
