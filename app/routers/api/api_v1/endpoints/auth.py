from fastapi import APIRouter
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
async def login(id, pw):
    pass

@router.post('/jwt/register')
async def register(id, pw):
    pass

@router.post('/jwt/refresh')
async def refresh_token(aa):
    pass