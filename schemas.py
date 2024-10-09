from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class UserBase(BaseModel):
    email: str
    name: str
    username: str
    phone_number: Optional[str] = None
    address: Optional[str] = None
    birthdate: Optional[str] = None
    profile_picture: Optional[str] = None
    role: Literal['guest', 'user', 'admin']
    is_active: Optional[bool] = True
    is_2fa_enabled: Optional[bool] = False


class UserCreate(UserBase):
    password: str  # Senha será enviada no cadastro


class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    profile_picture: Optional[str] = None


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
