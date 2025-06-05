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

### Docker Setup

```bash
docker-compose up --build
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

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