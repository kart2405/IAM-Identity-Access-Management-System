# IAM-Identity-Access-Management-System
🔐 A secure, scalable Identity &amp; Access Management (IAM) backend built with FastAPI. Supports JWT auth, RBAC, multi-tenant architecture, and PostgreSQL integration. Dockerized and extensible for modern web apps.




## Features

- 🔐 JWT-based authentication with access and refresh tokens
- 👥 Multi-tenant support
- 🔑 Role-based access control (RBAC)
- 🔄 Token revocation and session management
- 📧 Email verification
- 🔒 Password policies and security
- 📊 User activity logging
- 🚀 API rate limiting
- 🔍 Audit trails

## Project Roadmap

This project will be implemented in the following phases:

1. Scaffold FastAPI project structure (app, routers, models, services, utils, config)
2. Implement user registration, login, and JWT authentication
3. Set up PostgreSQL models and Alembic migrations (users, roles, permissions, tenants, sessions)
4. Add multi-tenant support (tenant isolation)
5. Implement RBAC and permissions system
6. Add email verification, password policies, and password hashing
7. Implement token revocation and session management (with Redis)
8. Add user activity logging and audit trails
9. Implement API rate limiting and CORS protection
10. Add input validation, SQL injection, and XSS prevention
11. Set up Docker and Docker Compose
12. Create environment variable management and example .env
13. Write Pytest test suite
14. Set up GitHub Actions for CI/CD
15. Document API endpoints and update README

## Tech Stack

- **Backend Framework**: FastAPI
- **Programming Language**: Python 3.11+
- **Authentication**: JWT (Access & Refresh Tokens)
- **Database**: PostgreSQL
- **ORM & Migrations**: SQLAlchemy + Alembic
- **Caching**: Redis
- **Data Validation**: Pydantic
- **Testing**: PyTest, HTTPX
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis
- Docker and Docker Compose (optional)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd iam-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run database migrations:
```bash
alembic upgrade head
```

6. Start the development server:
```bash
uvicorn app.main:app --reload
```

## Quickstart

After installing dependencies, you can run the development server with:

```bash
uvicorn app.main:app --reload
```

Or use Docker Compose:

```bash
docker-compose up --build
```

### Docker Setup

```bash
docker-compose up --build
```

## API Documentation

The API is fully documented and browsable via OpenAPI/Swagger and ReDoc:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Feature Status

- [x] JWT-based authentication (access & refresh tokens)
- [x] Multi-tenant support
- [x] Role-based access control (RBAC)
- [x] Token revocation and session management
- [x] Email verification (API ready, SMTP config required)
- [x] Password policies and security
- [x] User activity logging
- [x] API rate limiting
- [x] Audit trails
- [x] Docker & Docker Compose
- [x] CI/CD with GitHub Actions
- [x] Pytest test suite
- [x] OpenAPI/Swagger documentation

## Testing

Run the test suite:
```bash
pytest
```

## Security Features

- Password hashing using bcrypt
- JWT token encryption
- Rate limiting
- CORS protection
- Input validation
- SQL injection prevention
- XSS protection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. # IAM-Identity-Access-Management-System