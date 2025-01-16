from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserSimple(BaseModel):
    id: Optional[int] = None
    first_name: str
    email: str

    class Config:
        from_attributes = True


class Login(BaseModel):
    email: str
    password: str


class LoginSucces(BaseModel):
    user: UserSimple
    token: str
