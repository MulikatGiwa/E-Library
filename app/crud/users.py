from fastapi import Body, HTTPException,status
from app.schemas.users import User, UserCreate, UserLogin, UserUpdate
from app.database.users import Users
from typing import Annotated

class UserCrud:

    @staticmethod
    def signup(user:UserCreate, confirm_password: Annotated [str, Body()]):
        for Id, user_data in Users.items():
            if  user_data["email"] == user.email:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
        if user.password != confirm_password:
            raise HTTPException(status.HTTP_409_CONFLICT, detail= "passwords do not match")
        user_id = len(Users)+1
        new_user=User(id=user_id, **user.model_dump())
        Users[user_id]= new_user.model_dump()
        return new_user
    
    @staticmethod
    def login(user:UserLogin):
        for id, user_data in Users.items():
            if user_data["email"] != user.email or user_data["password"] != user.password:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Invalid email or password")
            if user_data["email"] == user.email and user_data["password"] == user.password:
                return

    @staticmethod
    def get_users():
        return Users

    @staticmethod
    def get_user(user_id:int):
        user=Users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found")
        return user
    
    @staticmethod
    def update_user(user_id:int, update_data:UserUpdate):
        updated_user = Users.get(user_id)
        if not updated_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found")
        for key, values in update_data.model_dump(exclude_unset=True).items():
            if key in updated_user:
                updated_user[key] = values
            return updated_user
    
    @staticmethod
    def delete_user(user_id:int):
        deleted_user = Users.get(user_id)
        if not deleted_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found")
        del Users[user_id]
        return

user_crud = UserCrud()