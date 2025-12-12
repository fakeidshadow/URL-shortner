# Complete Midterm Project Report: URL Shortener System

## Project Specifications
- Title: URL Shortener System
- Course: Software Engineering
- University: AUT
- Date: December 2025
- Project Type: Team-based (Two Members)

## Project Objectives
Implementation of a professional backend service practicing:
- Layered Architecture Design
- Relational Database Management (PostgreSQL)
- RESTful API Implementation Principles
- Dependency Management with Constructor Injection
- Error Handling and Documentation

## System Architecture
### Architecture Layers:
1. Controller Layer (API Interface)
2. Service Layer (Business Logic)
3. Repository Layer (Data Access)

## Technologies Used
Technology | Version | Purpose
-----------|---------|---------
Python | 3.9+ | Main Programming Language
FastAPI | 0.104.0 | Main API Framework
SQLAlchemy | 2.0.0 | Database ORM
PostgreSQL | 15+ | Relational Database
Alembic | 1.12.0 | Migration Management
Poetry | 1.5+ | Dependency Management
Git/GitHub | - | Version Control
Postman | - | API Testing

## Database Structure
### Table `urls`:
Column | Data Type | Description
-------|-----------|------------
id | Integer | Primary Key
original_url | String | Original Long URL
short_code | VARCHAR(10) | Unique Short Code
created_at | DateTime | Creation Timestamp
expires_at | DateTime | Expiration Time (Optional)

## API Endpoints

### 1. Create Short Link
POST /links
Request:
{"original_url": "https://example.com/very/long/url"}
Success Response (201):
{
  "status": "success",
  "data": {
    "id": 1,
    "original_url": "https://example.com/very/long/url",
    "short_url": "https://short.ly/abc123",
    "short_code": "abc123",
    "created_at": "2024-01-01T12:30:00"
  }
}

### 2. Redirect to Original URL
GET /{short_code}
Behavior: Redirects to original URL with 302 Found status.

### 3. View All Shortened Links
GET /links
Response:
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "original_url": "https://example.com",
      "short_code": "abc123",
      "created_at": "2024-01-01T12:30:00"
    }
  ]
}

### 4. Delete Short Link
DELETE /links/{short_code}
Success Response (200):
{
  "status": "success",
  "message": "URL deleted successfully"
}

## Implemented Technical Requirements
- Layered Architecture: Complete separation of Controller, Service, Repository
- Constructor Injection: Dependency injection between layers
- Error Management: Comprehensive error handling with HTTP status codes
- RESTful Principles: Proper use of HTTP verbs and resource naming
- Security: Input validation, SQL injection prevention

## Short Code Generation Method
Uses ID-based Base62 Conversion:
1. Record saved in database
2. ID converted to Base62
3. Inherent uniqueness guarantee
Advantages: High performance, guaranteed uniqueness, recoverability

## Project Execution Guide
Clone and setup:
git clone https://github.com/fakeidshadow/URL-shortner.git
cd URL-shortner
poetry install
poetry shell
cp .env.example .env
Run migrations and start server:
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## Testing & Documentation
- Postman Tests: All 4 endpoints tested
- Screenshots: Success and error responses documented
- API Documentation: Complete endpoint documentation

## Team Responsibilities
Task | Responsible Member
-----|-------------------
Database Setup & Models | Member 1
Repository Implementation | Member 1
Service Layer | Member 2
Controller & API | Member 2
Testing & Documentation | Both

## Final Checklist
[x] 3-Layer Architecture
[x] Constructor Injection
[x] 4 Complete Endpoints
[x] Error Management
[x] API Documentation
[x] Postman Testing
[x] Screenshots
[x] Complete README
[x] GitHub Upload

## File Structure
URL-shortner/
├── app/
│   ├── controllers/link_controller.py
│   ├── services/link_service.py
│   ├── repositories/link_repository.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── main.py
├── migrations/
├── tests/
├── postman/
├── .env.example
├── pyproject.toml
├── alembic.ini
└── README.md

## Bonus Features Implemented
- TTL (Time To Live): Automatic link expiration
- Base62 Encoding: Optimized code generation
- Comprehensive Error Handling
- Complete Documentation

## Future Development
- User Authentication
- Rate Limiting
- Visit Statistics
- Web Interface
- Dockerization

Delivery Date: December 2025
Development Team: [Team Name]
Course Instructor: [Instructor Name]
Expected Grade: [Expected: 20/20]
