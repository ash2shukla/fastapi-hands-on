# 1. FastAPI is a starlette wrapper for ASGI compatible http app dev in python
# 2.Create an app
from fastapi import FastAPI

app = FastAPI()

# 3. create some model for payload
from pydantic import BaseModel


class Point(BaseModel):
    x: float
    y: float


# 4. add routes
@app.post("/{path_param}")
async def hello(path_param: str, query_param: int, payload: Point):
    return {"path_param": path_param, "query_param": query_param, "payload": payload}


if __name__ == "__main__":
    # 5. Get an ASGI web server eg. hypercorn (h3), uvicorn (h1/h2)
    import uvicorn

    # 6. Pass the app and run !
    uvicorn.run(app)

    # 7. Or you can use cli of uvicorn and pass refernce and args to run from there
    # eg. uvicorn main:app --workers=4... bla bla
