from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth_router, tenant_router, role_router, session_router
from app.middleware.rate_limit import RateLimiter


app = FastAPI(title="IAM Identity & Access Management System")

app.add_middleware(RateLimiter)

# CORS setup (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(tenant_router)
app.include_router(role_router)
app.include_router(session_router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the IAM Identity & Access Management System API"
    }
