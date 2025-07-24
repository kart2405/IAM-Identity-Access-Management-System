from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.role import Role, user_roles
from app.models.user import User
from app.utils.db import get_db
from app.schemas.role import RoleCreate, RoleOut, AssignRole
from app.services.auth import get_current_user

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/", response_model=RoleOut)
def create_role(role_in: RoleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    role = Role(name=role_in.name, description=role_in.description, tenant_id=role_in.tenant_id)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

@router.get("/", response_model=list[RoleOut])
def list_roles(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Role).filter(Role.tenant_id == current_user.tenant_id).all()

@router.post("/assign", status_code=204)
def assign_role(assign: AssignRole, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    user = db.query(User).filter(User.id == assign.user_id, User.tenant_id == current_user.tenant_id).first()
    role = db.query(Role).filter(Role.id == assign.role_id, Role.tenant_id == current_user.tenant_id).first()
    if not user or not role:
        raise HTTPException(status_code=404, detail="User or Role not found")
    db.execute(user_roles.insert().values(user_id=user.id, role_id=role.id))
    db.commit() 