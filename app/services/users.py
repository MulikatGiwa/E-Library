from fastapi import HTTPException,status
from app.database.users import Users


class UserService:

    @staticmethod
    def deactivate_user(user_id:int):
        deactivated_user = Users.get(user_id)
        if not deactivated_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found")
        if deactivated_user.is_active != True:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "User is not active")
        deactivated_user.is_active = False
        return deactivated_user

user_service = UserService ()
