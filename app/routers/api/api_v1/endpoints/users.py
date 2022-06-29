from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import create_user, get_users, get_user, get_user_by_employee_id, update_user, delete_user
from app.routers.api.deps import get_db, get_current_user, get_current_active_superuser, get_current_active_user
from app.schemas.user import User, UserCreate, UserUpdate, UserMe

router = APIRouter()


@router.post("/", response_model=User)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    register_user = get_user_by_employee_id(db, user.employee_id)
    if register_user:
        raise HTTPException(status_code=401, detail="user already exist")
    user = create_user(db, user)
    return {"result": True, "employee_id": user.employee_id}



@router.get("/me", response_model=UserMe)
async def read_user(user:User = Depends(get_current_user)):
    userMe = UserMe(
        id = user.id,
        username = user.username,
        employee_id = user.employee_id,
        auth = user.auth,
        belong_1 = user.belong_1,
        belong_2 = user.belong_2,
        belong_3 = user.belong_3,
        belong_4 = user.belong_4,
    )
    return userMe
    # return {"employee_id": user.employee_id}


@router.get("/", response_model=List[UserUpdate])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user:User = Depends(get_current_active_superuser)):
    print(user.employee_id)
    users = get_users(db, skip=skip, limit=limit)
    print("USERS: ", users[0].auth)
    users_out = list(map(lambda model:
        UserUpdate(
            id=model.id,
            employee_id=model.employee_id,
            password=model.hashed_password,
            username=model.username,
            email=model.email,
            phone=model.phone,
            is_active=model.is_active,
            is_superuser=model.is_superuser,

            auth=model.auth,
            belong_1=model.belong_1,
            belong_2=model.belong_2,
            belong_3=model.belong_3,
            belong_4=model.belong_4,
        ), users))

    print("USER[0].auth: ", users_out[0].auth)
    print(users_out[0])
    return users_out

@router.get("/{id}", response_model=User)
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/emp/{id}", response_model=User)
async def read_user_by_empid(id: str, db: Session = Depends(get_db)):
    db_user = get_user_by_employee_id(db, employee_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.patch("/{id}", response_model=User)
async def update_user_by_id(id: int, user:UserUpdate, db: Session = Depends(get_db),
                      client=Depends(get_current_active_user)):
    if not client.is_superuser:
        if client.id != id:
            raise HTTPException(status_code=401, detail="Need Auth...")
    _user = update_user(db, user_id=id, user=user)

    return {"result": "Update Success!", "id": _user.id}


@router.delete("/{id}", response_model=User)
async def delete_user_by_id(id: int, db: Session = Depends(get_db),
                      client=Depends(get_current_active_user)):
    if not client.is_superuser:
        if client.id != id:
            raise HTTPException(status_code=401, detail="Need Auth...")
    _ = delete_user(db=db, user_id=id)
    return {"result": "Delete Success!"}

