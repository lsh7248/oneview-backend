from sqlalchemy.orm import Session

from .. import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    # DB ID 쿼리 후, 가장 큰 ID값을 찾아서 +1 한 ID 값을 ID로 지정
    # db.query(models.User).order_by

    db_user = models.User(id=2, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_superuser(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"

    db_user = models.User(id=1, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
