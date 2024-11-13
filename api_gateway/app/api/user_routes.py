from fastapi import APIRouter
from app.models.user import User
from app.services import user_service

router = APIRouter()

@router.get("/users")
def get_users(id: str = None):
    return user_service.get_users(id)

@router.post("/users")
def create_user(user: User):
    return user_service.create_user(user)

@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    return user_service.update_user(user_id, user)

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    return user_service.delete_user(user_id)