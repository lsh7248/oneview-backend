from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.crud.user import get_user_by_employee_id, create_user
from app.routers.api.deps import get_db, get_current_active_user, get_current_user
from app.schemas import UserCreate
from app.schemas.user import User

# class Settings(BaseModel):
#     authjwt_secret_key: str = "secret"
#
# @AuthJWT.load_config
# def get_config():
#     return Settings()


router = APIRouter()


@router.post('/jwt')
async def test(aaa):
    pass


@router.post('/jwt/login')
async def login(user: User, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    login_user = get_user_by_employee_id(db, user.employee_id)
    if not login_user:
        raise HTTPException(status_code=401,detail="Bad user id")
    if not verify_password(user.password, login_user.hashed_password):
        raise HTTPException(status_code=401,detail="Bad password")

    access_token = Authorize.create_access_token(subject=user.employee_id)
    refresh_token = Authorize.create_refresh_token(subject=user.employee_id)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post('/jwt/register')
async def register(user: UserCreate, db: Session = Depends(get_db)):
    register_user = get_user_by_employee_id(db, user.employee_id)
    if register_user:
        raise HTTPException(status_code=401, detail="user already exist")
    user = create_user(db, user)
    return {"state": True, "employee_id": user.employee_id}

@router.post('/jwt/refresh')
async def refresh(aa):
    pass