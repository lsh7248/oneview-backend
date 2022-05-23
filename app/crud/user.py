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
    hashed_password = get_password_hash(user.password)
    # DB ID 쿼리 후, 가장 큰 ID값을 찾아서 +1 한 ID 값을 ID로 지정
    recent_user:schemas.User = db.query(models.User).order_by(models.User.id.desc()).first()

    db_user = models.User(id=recent_user.id + 1,
                          employee_id=user.employee_id,
                          hashed_password=hashed_password,
                          username=user.username,
                          email=user.email,
                          phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_superuser(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)

    db_user = models.User(id=1,
                          employee_id=user.employee_id,
                          username=user.username,
                          email=user.email,
                          phone=user.phone,
                          hashed_password=hashed_password,
                          is_active=True,
                          is_superuser=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
