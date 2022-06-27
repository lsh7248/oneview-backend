from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..core.security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_employee_id(db: Session, employee_id: str):
    return db.query(models.User).filter(models.User.employee_id == employee_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    print("CREATE USER START")
    hashed_password = get_password_hash(user.password)
    # DB ID 쿼리 후, 가장 큰 ID값을 찾아서 +1 한 ID 값을 ID로 지정
    try:
        recent_user:schemas.User = db.query(models.User).order_by(models.User.id.desc()).first()
        input_id = recent_user.id + 1
    except:
        input_id = 1

    db_user = models.User(id=input_id,
                          employee_id=user.employee_id,
                          hashed_password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_superuser(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)

    db_user = models.User(id=1,
                          employee_id=user.employee_id,
                          # username=user.username,
                          # email=user.email,
                          # phone=user.phone,
                          hashed_password=hashed_password,
                          is_active=True,
                          is_superuser=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # 1. PASSWORD가 존재할 시, HASH
    if user.password:
        user.password = get_password_hash(user.password)

    user_data = user.dict(exclude_unset=True)
    for k, v in user_data.items():
        setattr(db_user, k, v)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user
