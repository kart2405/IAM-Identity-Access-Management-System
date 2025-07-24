import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import text
import uuid

client = TestClient(app)

def get_token(email, password, tenant_id=1, tenant_name=None):
    if tenant_name is None:
        tenant_name = f"TestTenant_{uuid.uuid4().hex[:8]}"
    from app.utils.db import SessionLocal
    db = SessionLocal()
    db.execute(text("INSERT OR IGNORE INTO tenants (id, name) VALUES (:id, :name)"), {"id": tenant_id, "name": tenant_name})
    db.commit()
    db.close()
    client.post("/auth/register", json={"email": email, "password": password, "tenant_id": tenant_id})
    db = SessionLocal()
    db.execute(text("UPDATE users SET is_superuser=1 WHERE email=:email"), {"email": email})
    db.commit()
    db.close()
    resp = client.post("/auth/login", json={"email": email, "password": password})
    return resp.json()["access_token"], tenant_name

def test_tenant_crud():
    token, tenant_name = get_token("super@tenant.com", "superpass")
    new_tenant_name = f"TestTenant_{uuid.uuid4().hex[:8]}"
    # Create tenant
    resp = client.post("/tenants/", json={"name": new_tenant_name}, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    # List tenants
    resp = client.get("/tenants/", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    assert any(t["name"] == new_tenant_name for t in resp.json()) 