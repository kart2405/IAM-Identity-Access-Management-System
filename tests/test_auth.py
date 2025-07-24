import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import text
import uuid

client = TestClient(app)

def test_register_and_login():
    email = f"pytestuser_{uuid.uuid4().hex[:8]}@example.com"
    password = "pytestpass123"
    tenant_id = 1
    # Ensure tenant exists
    from app.utils.db import SessionLocal
    db = SessionLocal()
    db.execute(text("INSERT OR IGNORE INTO tenants (id, name) VALUES (:id, :name)"), {"id": tenant_id, "name": "TestTenant"})
    db.commit()
    db.close()
    # Register
    response = client.post("/auth/register", json={"email": email, "password": password, "tenant_id": tenant_id})
    assert response.status_code == 200
    tokens = response.json()
    assert "access_token" in tokens
    # Login
    response = client.post("/auth/login", json={"email": email, "password": password})
    assert response.status_code == 200
    tokens = response.json()
    assert "access_token" in tokens 