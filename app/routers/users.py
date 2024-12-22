from typing import Annotated
from fastapi import APIRouter, Body,status
from app.schemas.users import UserCreate, UserLogin, UserUpdate
from app.crud.users import user_crud
from app.services.users import user_service

user_router = APIRouter()

@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user:UserCreate, confirm_password: Annotated [str, Body()]):
    new_user = user_crud.signup(user,confirm_password)
    return {"message": "Signup Successful", "data": new_user}

@user_router.post("/login", status_code=status.HTTP_200_OK)
def login(user:UserLogin):
    user_crud.login(user)
    return {"message": "Login Successful"}
        
@user_router.get("/users", status_code=status.HTTP_200_OK)
def get_users():
    Users=user_crud.get_users()
    return {"message": "Successful", "data": Users}

@user_router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id:int):
    user = user_crud.get_user(user_id)
    return {"message": "Successful", "data": user}

@user_router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id:int, update_data:UserUpdate):
    updated_user = user_crud.update_user(user_id, update_data)
    return {"message": "User Updated Successfully", "data": updated_user}

@user_router.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def deactivate_user(user_id:int):
    deactivated_user = user_service.deactivate_user(user_id)
    return {"message": "User Deactivated Successfully", "data": deactivated_user}

@user_router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id:int):
    user_crud.delete_user(user_id)
    return {"message": "User Deleted Successfully"}
