from core.database import database
from core.models import users
from core.shema import CreateUser, SignIn
from sqlalchemy import select, and_
from pydantic import EmailStr

async def email_exists_in_db(email: EmailStr) -> bool:
    query = select(users).where(users.c.email == email)
    result = await database.fetch_one(query)
    return result is not None

async def create_user_in_db(user : CreateUser):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    return await database.execute(query)

async def sign_in_db(user: SignIn):
    query = select(users).where(
        and_(
            users.c.email == user.email,
            users.c.password == user.password
        )
    )
    return await database.fetch_one(query)