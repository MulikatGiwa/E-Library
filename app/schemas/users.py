from typing import Optional
from pydantic import BaseModel

class UserBase (BaseModel):
    name: str
    email: str
    password: str
    
class User (UserBase):
    id: int
    is_active: bool = True


class UserCreate (UserBase):
    pass

class UserLogin (BaseModel):
    email: str
    password: str

class UserUpdate(UserBase):
    pass
