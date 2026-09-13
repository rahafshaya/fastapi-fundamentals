from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Fundamentals"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/search")
def search(q: str):
    return {"query": q}


class User(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {
        "message": "User updated",
        "user_id": user_id,
        "user": user
    }
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted",
        "user_id": user_id
    }