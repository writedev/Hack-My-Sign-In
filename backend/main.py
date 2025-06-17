from fastapi import FastAPI
from api.sign import router as sign_router

app = FastAPI()

app.include_router(sign_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)