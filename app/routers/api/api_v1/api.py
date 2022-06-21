from fastapi import APIRouter, Depends
from .endpoints import auth, users, items, voc
from ..deps import get_current_user

api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/api/v1", tags=["auth"])
api_v1_router.include_router(users.router, prefix="/api/v1/users", tags=["users"])
api_v1_router.include_router(items.router, prefix="/api/v1/items", tags=["items"])
api_v1_router.include_router(voc.router, prefix="/api/v1/vocs", tags=["vocs"])