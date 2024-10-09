from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # Armazenar a senha de forma segura (hash)
    phone_number = Column(String, nullable=True)
    address = Column(String, nullable=True)
    birthdate = Column(String, nullable=True)
    profile_picture = Column(String, nullable=True)
    role = Column(String, default="user")  # Ex: "admin", "user"
    is_active = Column(Boolean, default=True)
    is_2fa_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)