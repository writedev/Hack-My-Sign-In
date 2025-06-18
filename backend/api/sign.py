from fastapi import APIRouter, Depends
from core.crud import *
from core.shema import CreateUser, SignIn
from fastapi.responses import JSONResponse
from asyncmy import errors
from fastapi.exceptions import HTTPException
from pydantic import EmailStr
from core.encryp import create_jwt
from core.encryp import get_current_user


router = APIRouter(
    prefix="/sign",
    tags=["sign"],
)

@router.get("/verify_email")
async def verify_email_route(email: EmailStr):
    """
    Verify if an email exists in the database.
    """

    try:
        exists = await email_exists_in_db(email)

        if not exists:
            return JSONResponse(status_code=200, content={"message": "User does not exist!"})
        else:
            return JSONResponse(status_code=409, content={"message": "User exists!"})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create_user")
async def root(data : CreateUser):
    try:
        await create_user_in_db(data)
        return JSONResponse(status_code=200, content={"message": "User created successfully!"})
    except errors.IntegrityError:
        return JSONResponse(status_code=400, content={"message": "User already exists!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/sign_in")
async def sign_in(data: SignIn):
    user = await sign_in_db(data)

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    print(user[0])
    token = create_jwt(user[0])

    return JSONResponse(status_code=200, content={"acess_token": token})

@router.get("/test")
async def get_user_docs(user_id: str = Depends(get_current_user)):
    return {"user_id": user_id}