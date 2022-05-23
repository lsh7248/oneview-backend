from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import create_user, get_users, get_user, get_user_by_employee_id
from app.routers.api.deps import get_db
from app.schemas.user import User, UserCreate

router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_employee_id(db, employee_id=user.employee_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return create_user(db=db, user=user)


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{id}", response_model=User)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/emp/{id}", response_model=User)
def read_user_by_empid(id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_employee_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user