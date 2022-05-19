from fastapi import APIRouter
from .endpoints import auth

api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/api/v1", tags=["auth"])

# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])