from uuid import UUID
from models.users import User, Gender, Role
from typing import List
from fastapi import FastAPI, HTTPException

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("fce3429a-0533-4e8a-8282-5cd9bfd78edb"),
        first_name="Pranay",
        last_name="Bankar",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    
    User(
        id=UUID("d236273c-0f03-49ae-80f6-edd289acc70e"),
        first_name="Snehal",
        last_name="Bankar",
        gender=Gender.female,
        roles=[Role.user, Role.student]
    )
]

@app.get("/")
async def hello():
    return "Welcome to User page."

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist."
    )