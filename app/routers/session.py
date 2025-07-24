from fastapi import APIRouter, Depends, HTTPException, status
from app.services.session import SessionService
from app.services.auth import get_current_user, AuthService
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt
from app.config import settings
from app.services.logging import LoggingService

router = APIRouter(prefix="/sessions", tags=["sessions"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/logout", status_code=204)
def logout(current_user: User = Depends(get_current_user), token: str = Depends(oauth2_scheme)):
    payload = AuthService.verify_token(token)
    if not payload or "jti" not in payload:
        raise HTTPException(status_code=400, detail="Invalid token")
    SessionService.revoke_token(payload["jti"])
    LoggingService.log_event(current_user.id, "logout", f"jti={payload['jti']}")

@router.get("/check/{jti}")
def check_token(jti: str):
    if SessionService.is_token_revoked(jti):
        return {"revoked": True}
    return {"revoked": False} 