from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from passlib.context import CryptContext

# Configuração para hashing de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_all_users(db: Session):
    return db.query(models.User).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    if user.role not in ['guest', 'user', 'admin']:
        raise HTTPException(status_code=400, detail="Invalid role")

    db_user = models.User(
        email=user.email,
        name=user.name,
        username=user.username,
        password=user.password,  # Certifique-se de hashear a senha
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verifica se o usuário é um admin
    if db_user.role == "admin":
        raise HTTPException(status_code=403, detail="Cannot delete an admin user")

    # Exclusão lógica: define is_active como False
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)

    return db_user
