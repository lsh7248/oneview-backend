from typing import List, Union
from .item import Item
from pydantic import BaseModel
from app.models.user import UserAuthority


class UserBase(BaseModel):
    employee_id: Union[str, None]
    password: Union[str, None]
    # username: Union[str, None]
    # email: Union[str, None]
    # phone: Union[str, None]


class UserCreate(UserBase):
    # employee_id: str
    # id: Union[int, None]
    password: Union[str, None]
    # username: Union[str, None] = None
    # email: Union[str, None] = None
    # phone: Union[str, None] = None



class UserUpdate(UserBase):
    id: Union[int, None]
    password: Union[str, None]
    username: Union[str, None] = None
    email: Union[str, None] = None
    phone: Union[str, None] = None
    is_active: Union[bool, None] = None
    is_superuser: Union[bool, None] = None

    auth: UserAuthority = None # serAuthority
    belong_1: Union[str, None] = None
    belong_2: Union[str, None] = None
    belong_3: Union[str, None] = None
    belong_4: Union[str, None] = None


class UserInDBBase(UserBase):
    id: Union[int, None]
    is_active: Union[bool, None] = None
    is_superuser: Union[bool, None] = None
    items: List[Item] = []

    class Config:
        orm_mode = True

class UserMe(BaseModel):
    id: Union[int, None]
    employee_id: Union[str, None]
    username: Union[str, None] = None
    auth: UserAuthority = None  # serAuthority
    belong_1: Union[str, None] = None
    belong_2: Union[str, None] = None
    belong_3: Union[str, None] = None
    belong_4: Union[str, None] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "employee_id": "10151032",
                "auth": "직원",
                "belong_1": "네트워크부문",
                "belong_2": "네트워크운용혁신담당",
                "belong_3": "네트워크운용혁신담당",
                "belong_4": "네트워크AI개발P-TF",

            }
        }


class User(UserBase):
    id: Union[int, None]

    class Config:
        schema_extra={
            "example":{
                "employee_id": "10151032",
                "auth": "직원",
                "belong_1": "네트워크부문",
                "belong_2": "네트워크운용혁신담당",
                "belong_3": "네트워크운용혁신담당",
                "belong_4": "네트워크AI개발P-TF",

            }
        }



class UserInDB(UserInDBBase):
    hashed_password: str