from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import crud
import models
import schemas
from database import SessionLocal, engine

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verifica se o email já está registrado
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Verifica se o username já está em uso
    db_username = crud.get_user_by_username(db, username=user.username)
    if db_username:
        raise HTTPException(status_code=400, detail="Username not available")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user_name(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    # Atualiza apenas os campos permitidos
    if user_update.name:
        db_user.name = user_update.name
    if user_update.phone_number:
        db_user.phone_number = user_update.phone_number
    if user_update.address:
        db_user.address = user_update.address
    if user_update.profile_picture:
        db_user.profile_picture = user_update.profile_picture
    db.commit()
    db.refresh(db_user)
    return db_user


# Rota para deletar um usuário (exclusão lógica)
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)