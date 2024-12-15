from typing import Annotated
from fastapi import APIRouter, Body, HTTPException,status
from app.database.users import Users
from app.schemas.users import User, UserCreate, UserLogin, UserUpdate
from app.crud.users import user_crud

user_router = APIRouter()

@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user:UserCreate, confirm_pasword: Annotated [str, Body()]):
    new_user = user_crud.signup(user,confirm_pasword)
    return {"message": "Signup Succesful", "data": new_user}

@user_router.post("/login", status_code=status.HTTP_200_OK)
def login(user:UserLogin):
    user_crud.login(user)
    return {"message": "Login Successful"}
        
@user_router.get("/users", status_code=status.HTTP_200_OK)
def get_users():
    Users=user_crud.get_users()
    return {"message": "Succesful", "data": Users}

@user_router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id:int):
    user = user_crud.get_user(user_id)
    return {"message": "Succesful", "data": user}

@user_router.put("/users/{user_id}")
def update_user(user_id:int, update_data:UserUpdate):
    updated_user = user_crud.update_user(user_id, update_data)
    return {"message": "User updated Succesfully", "data": updated_user}

@user_router.patch("/users/{user_id}")
def deactivate_user(user_id:int):
    deactivated_user = user_crud.deactivate_user(user_id)
    return {"message": "User deactivated Succesfully", "data": deactivated_user}

@user_router.delete("/users/{user_id}")
def delete_user(user_id:int):
    user_crud.delete_user(user_id)
    return {"message": "User deleted successfully"}
