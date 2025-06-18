from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password : str

class SignIn(BaseModel):
    email : EmailStr
    password : str
