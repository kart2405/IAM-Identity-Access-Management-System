from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str
    description: str | None = None
    tenant_id: int

class RoleOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    tenant_id: int
    class Config:
        from_attributes = True

class AssignRole(BaseModel):
    user_id: int
    role_id: int 