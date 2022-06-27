import logging
from sqlalchemy.orm import Session
#  환경변수
import os
from dotenv import load_dotenv

from app.core.security import get_password_hash
from app.crud.user import get_user_by_employee_id, create_superuser
from app.db.session import engine
from app.schemas.user import UserCreate
from app.db import base  # noqa: F401
from app.db.base import Base, KBase

logger = logging.getLogger(__name__)
load_dotenv()
# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

FIRST_SUPERUSER_ID = os.environ.get("FIRST_SUPERUSER_ID")
FIRST_SUPERUSER_NAME = os.environ.get("FIRST_SUPERUSER_NAME")
FIRST_SUPERUSER_EMAIL = os.environ.get("FIRST_SUPERUSER_EMAIL")
FIRST_SUPERUSER_PW = os.environ.get("FIRST_SUPERUSER_PW")

# def create_superuser(db: Session) -> None:
#     print("metadata Create Table init...")
#     Base.metadata.create_all(bind=engine)
#     print("metadata Create Table Suc!!!!")
#     user_in = UserCreate(
#         # id=1,
#         employee_id=FIRST_SUPERUSER_ID,
#         password=FIRST_SUPERUSER_PW,
#         email=FIRST_SUPERUSER_EMAIL,
#         username=FIRST_SUPERUSER_NAME,
#         is_superuser=True,
#     )
#     print(type(user_in))
#     create_user(db, user_in)

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)
    # In Development version --> KDAP DB Model Create
    KBase.metadata.create_all(bind=engine)

    if FIRST_SUPERUSER_ID:
        superuser = get_user_by_employee_id(db=db, employee_id=FIRST_SUPERUSER_ID)  # 2
        if not superuser:
            user_in = UserCreate(
                employee_id=FIRST_SUPERUSER_ID,
                username=FIRST_SUPERUSER_NAME,
                email=FIRST_SUPERUSER_EMAIL,
                password=FIRST_SUPERUSER_PW,
                # email=FIRST_SUPERUSER_EMAIL,
                # username=FIRST_SUPERUSER_NAME,
                # is_superuser=True,
            )
            create_superuser(db, user_in)
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{FIRST_SUPERUSER_ID} already exists. "
            )
