# Bookstore API

A RESTful API code sample for managing a bookstore with user roles and book inventory management. Built with Flask, SQLAlchemy, and MySQL, containerized with Docker.

## 🚀 Features

- **Book Management**: Full CRUD operations for book inventory
- **User Management**: User registration and profile management
- **Role-Based Access**: Admin and user role system
- **Containerized**: Docker-ready with development and production setups

## 🛠 Dependencies

- **Backend**: Flask 2.2.5, SQLAlchemy 2.0.23
- **Database**: MySQL with PyMySQL driver
- **Serialization**: Marshmallow for data validation and serialization
- **Containerization**: Docker & Docker Compose
- **Environment**: Python 3.8+

## 🏃‍♂️ Quick Start

### Using Docker

1. **Clone the repository**
```bash
git clone <repository-url>
cd bookstore
```

2. **Start the services**
```bash
docker compose build && docker compose up -d
```

4. **Initialize the database**
```bash
docker exec api flask setup all
```

The API will be available at `http://localhost:50000`


## 🗄 Database Schema

### Core Models

- **Book**: Book inventory with title, author, and ISBN
- **User**: User profiles with first and last names
- **Role**: System roles (admin, user)
- **UserRole**: Many-to-many relationship between users and roles

## 🔧 CLI Commands

### Database Setup
```bash
# Create all database tables
flask setup create-tables

# Insert demo data (2 users, 2 roles, 3 books)
flask setup insert-demo-data

# Complete setup (create tables + demo data)
flask setup all
```

### Demo Data Includes
- **Roles**: admin, user
- **Users**: Admin User (admin role), Regular User (user role)
- **Books**: The Little Prince, Learning Python, Unwinding Anxiety

## 📚 API Documentation

### Base URL
- Development: `http://localhost:50000`
- All endpoints are prefixed with `/v1`

### Books API

#### Get All Books
```http
GET /v1/books?page=1&per_page=10
```

**Response:**
```json
{
  "books": [
    {
      "uuid": "123e4567-e89b-12d3-a456-426614174000",
      "title": "The Little Prince",
      "author": "Antoine de Saint-Exupéry",
      "isbn": "978-0152023980",
      "created_at": "2024-01-01T00:00:00",
      "updated_at": "2024-01-01T00:00:00"
    }
  ],
  "pagination": {
    "page": 1,
    "pages": 1,
    "per_page": 10,
    "total": 3,
    "has_next": false,
    "has_prev": false
  }
}
```

#### Get Single Book
```http
GET /v1/books/{uuid}
```

#### Create Book
```http
POST /v1/books
Content-Type: application/json

{
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "978-1234567890"
}
```

#### Update Book
```http
PUT /v1/books/{uuid}
Content-Type: application/json

{
  "title": "Updated Title",
  "author": "Updated Author",
  "isbn": "978-0987654321"
}
```

#### Delete Book
```http
DELETE /v1/books/{uuid}
```

## 🐳 Docker Configuration

### Services

- **api**: Flask application (port 50000)
- **db**: MySQL database (port 33060)

### Environment Variables

This is a coding sample. Therefore, the `.env` file is intentionally left in for ease of setup. PLEASE DO NOT SUBMIT YOUR `.env` FILE TO YOUR REPO IN PRACTICE.

## TODO

- Add authentication and role based access control
- Add tests
