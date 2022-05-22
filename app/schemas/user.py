from typing import List
from .item import Item
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = None
    items: List[Item] = []

    class Config:
        orm_mode = True