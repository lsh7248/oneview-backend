from fastapi import APIRouter
from .endpoints import auth, users, items
    # , user

api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/api/v1", tags=["auth"])
api_v1_router.include_router(users.router, prefix="/api/v1/users", tags=["user"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
api_v1_router.include_router(items.router, prefix="/api/v1/items", tags=["items"])
