import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_jwt(user_id: str):
    """
    Create a JSON Web Token (JWT) for a user.

    Args:
        user_id (str): The ID of the user for whom the token is being created.

    Returns:
        str: A JWT as a string that includes the user's ID and an expiration time set to 60 minutes from now.
    """

    payload = {
        "id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=60)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get the current user from the Authorization header.

    Raises a 401 error if the token is invalid or expired.

    Returns the user ID.
    """
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["id"]  # l'ID de l'utilisateur
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")