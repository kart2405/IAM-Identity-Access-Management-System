from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.tenant import Tenant
from app.utils.db import get_db
from app.schemas.tenant import TenantCreate, TenantOut
from app.models.user import User
from app.services.auth import get_current_user

router = APIRouter(prefix="/tenants", tags=["tenants"])

@router.post("/", response_model=TenantOut)
def create_tenant(tenant_in: TenantCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    tenant = Tenant(name=tenant_in.name)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant

@router.get("/", response_model=list[TenantOut])
def list_tenants(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return db.query(Tenant).all()

@router.get("/{tenant_id}", response_model=TenantOut)
def get_tenant(tenant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    if not current_user.is_superuser and current_user.tenant_id != tenant_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return tenant 