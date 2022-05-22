from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .crud.user import create_user
from .db.init_db import init_db
from .db.session import SessionLocal, engine
from .db.base import Base
from .routers.api.api_v1.api import api_v1_router
from pydantic import BaseModel
# Base.metadata.create_all(bind=engine)
from .schemas import UserCreate


app = FastAPI()
# DB 초기화
init_db(SessionLocal())


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(api_v1_router)
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response
