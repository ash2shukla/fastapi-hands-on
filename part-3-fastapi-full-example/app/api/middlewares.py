import time

from fastapi import Request


async def record_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-new-header"] = str(time.time() - start_time)
    return response
