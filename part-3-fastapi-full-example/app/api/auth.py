from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

bearer = OAuth2PasswordBearer(tokenUrl="/token")


async def get_current_user(token: str = Depends(bearer)):
    print("Here is the token", token)
    return {"user_id": 1}
