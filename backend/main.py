from fastapi import FastAPI
from api.sign import router as sign_router
from core.database import database
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code executed at startup (startup)
    await database.connect()
    yield
    #codeExecutedAtTheStop (shutdown)
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(sign_router)