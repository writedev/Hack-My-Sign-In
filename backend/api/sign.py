from fastapi import APIRouter
from core.crud import *
from core.shema import CreateUser
from fastapi.responses import JSONResponse
from asyncmy import errors
from fastapi.exceptions import HTTPException
from pydantic import EmailStr


router = APIRouter(
    prefix="/sign",
    tags=["sign"],
)

@router.get("/verify_email")
async def verify_email_route(email: EmailStr):
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
        await create_user(data)
        return JSONResponse(status_code=200, content={"message": "User created successfully!"})
    except errors.IntegrityError:
        return JSONResponse(status_code=400, content={"message": "User already exists!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

