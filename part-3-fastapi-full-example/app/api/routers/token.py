from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/token")


@router.post("")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "user" and form_data.password == "pass":
        return {"access_token": "new_fake_token", "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401)
