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

def test_role_crud():
    token, tenant_name = get_token("super@role.com", "superpass")
    role_name = f"pytestrole_{uuid.uuid4().hex[:8]}"
    # Create role
    resp = client.post("/roles/", json={"name": role_name, "description": "desc", "tenant_id": 1}, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    # List roles
    resp = client.get("/roles/", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    assert any(r["name"] == role_name for r in resp.json())
    # Register a new user for assignment
    user_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    user_password = "userpass123"
    client.post("/auth/register", json={"email": user_email, "password": user_password, "tenant_id": 1})
    from app.utils.db import SessionLocal
    db = SessionLocal()
    user_id = db.execute(text("SELECT id FROM users WHERE email=:email"), {"email": user_email}).fetchone()[0]
    db.close()
    role_id = resp.json()[0]["id"]
    resp = client.post("/roles/assign", json={"user_id": user_id, "role_id": role_id}, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 204 