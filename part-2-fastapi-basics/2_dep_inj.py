# 1. But why fastapi then? quart can also do that and so can sanic.
# 2. Dependency Injection - Simple yet beautiful !

from fastapi import FastAPI

app = FastAPI()


# 3. Declare a callable that returns something


async def flat_dep():
    print("I got called !")
    return object()


# 4. import Depends from fastapi
from fastapi import Depends


# 5. While adding the route give it as a Depends(__callable__)
@app.get("/flat_dep")
async def flat_dep_ep(some_object=Depends(flat_dep)):
    print(some_object, id(some_object))
    return "flat_dep response"


# 6. Nested dependencies are resolved automatically !
async def call_context():
    print("call_context got called")


async def nested_dep(_=Depends(call_context)):
    print("nested_deps got called")


@app.get("/nested_dep")
async def nested_dep_ep(_=Depends(nested_dep)):
    return "nested_dep response"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
