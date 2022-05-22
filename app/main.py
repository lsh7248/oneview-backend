from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .crud.user import create_user
from .db.init_db import init_db
from .db.session import SessionLocal, engine
from .db.base import Base
from .routers.api.api_v1.api import api_v1_router

# Base.metadata.create_all(bind=engine)
from .schemas import UserCreate

app = FastAPI()
init_db(SessionLocal())
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

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

