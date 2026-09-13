# FastAPI Fundamentals

A beginner-friendly FastAPI project built to practice the fundamentals of API development using Python.

## Features

- REST API development with FastAPI
- GET, POST, PUT, and DELETE endpoints
- Path parameters
- Query parameters
- Request body validation with Pydantic
- Swagger API documentation
- Basic CRUD operations

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## Endpoints

- `GET /`
- `GET /health`
- `GET /users/{user_id}`
- `GET /search?q=fastapi`
- `POST /users`
- `PUT /users/{user_id}`
- `DELETE /users/{user_id}`

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
