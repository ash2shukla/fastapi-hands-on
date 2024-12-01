from contextlib import asynccontextmanager

from fastapi import FastAPI

from .routers import router as root_router


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

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api.main:create_app", factory=True, reload=True)
