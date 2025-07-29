import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django

from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from django.contrib.auth import authenticate

from datetime import datetime, timedelta
from jose import JWTError, jwt

from fastapi import Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 3

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject4.settings")

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject4.settings")
django.setup()

# from accounts.models import CustomUser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


from django.contrib.auth import get_user_model


@app.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    print(email)
    print(password)
    try:
        user = get_user_model().objects.get(email=email)
    except get_user_model().DoesNotExist:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    print(user.username)
    print(user.password)
    user = authenticate(username=user.username, password=password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "sub": str(user.id),
        "username": user.username,
        "email": user.email,
        "role": user.role,
    }
    token = create_access_token(data=payload)

    return {
        "access_token": token,
        "user": payload
    }


security = HTTPBearer()


def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception:
        return None


@app.get("/me")
def get_me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_jwt(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"user": payload}
