from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.auth import AuthService
from app.models.user import User
from app.config import settings
from app.utils.db import get_db
from app.schemas.auth import UserRegister, UserLogin, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=TokenResponse)
def register(user_in: UserRegister, db: Session = Depends(get_db)):
    existing = AuthService.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = AuthService.create_user(db, user_in.email, user_in.password, user_in.tenant_id)
    access_token = AuthService.create_access_token({"sub": user.email, "user_id": user.id})
    refresh_token = AuthService.create_refresh_token({"sub": user.email, "user_id": user.id})
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)

@router.post("/login", response_model=TokenResponse)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = AuthService.get_user_by_email(db, user_in.email)
    if not user or not AuthService.verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = AuthService.create_access_token({"sub": user.email, "user_id": user.id})
    refresh_token = AuthService.create_refresh_token({"sub": user.email, "user_id": user.id})
    return TokenResponse(access_token=access_token, refresh_token=refresh_token) 