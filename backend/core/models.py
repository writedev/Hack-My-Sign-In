from sqlalchemy import Table, Column, Integer, String
from .database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, unique=True, autoincrement=True),
    Column("username", String(100)),
    Column("email", String(100), unique=True),
    Column("password", String(100),),
)
