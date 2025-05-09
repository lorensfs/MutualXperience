from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
# from app.core.helper.scopes import get_scopes_from_db
from app.database.session import SessionLocal


def get_oauth2_scheme():
    session = SessionLocal()
    try:
        # scopes = get_scopes_from_db(session)
        return OAuth2PasswordBearer(
            tokenUrl=f"{settings.API_V1_STR}/login", #scopes=scopes
        )
    finally:
        session.close()


oauth2_scheme = get_oauth2_scheme()


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes_encoded = plain_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes_encoded, hashed_password.encode("utf-8"))


def hash_password(password: str) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode("utf-8")
