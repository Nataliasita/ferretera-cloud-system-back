# user_gateway/app/services/user_service.py
import requests
from fastapi import HTTPException
from app.core.config import USER_MS_URL
from app.models.user import User

def get_users(user_id=None):
    url = f"{USER_MS_URL}?id={user_id}" if user_id else USER_MS_URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())

def create_user(user: User):
    response = requests.post(USER_MS_URL, json=user.dict())
    if response.status_code == 201:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())

def update_user(user_id: str, user: User):
    data = user.dict()
    data['id'] = user_id
    response = requests.put(USER_MS_URL, json=data)
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())

def delete_user(user_id: str):
    response = requests.delete(USER_MS_URL, json={'id': user_id})
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail=response.json())