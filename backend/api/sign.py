from fastapi import APIRouter

router = APIRouter(
    prefix="/sign",
    tags=["sign"],
)

@router.get("/hi")
async def root():
    return {"message": "Hello World"}