from typing import Generator

from fastapi import HTTPException, Depends, status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from app import models
from app.core import security
# from app.core.config import settings
from app.crud.blacklist import get_blacklist
from app.crud.user import get_user_by_employee_id
from app.db.session import SessionLocal


#
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token, db: Session = Depends(get_db)):
    jti = decrypted_token['jti']
    token = get_blacklist(db, jti)
    return not not token


def get_current_user(
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> models.User:
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    employee_id = Authorize.get_jwt_subject()
    user = get_user_by_employee_id(db, employee_id)
    revoked_token = get_blacklist(db, Authorize.get_raw_jwt()['jti'])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    elif revoked_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Logout User",
        )
    return user
#
#
def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
#
#
def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user