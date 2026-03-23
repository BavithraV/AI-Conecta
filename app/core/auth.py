from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import jwt

security = HTTPBearer()


def get_current_user(credentials=Depends(security)):
    try:
        return jwt.decode(credentials.credentials, options={"verify_signature": False})
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
