from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.base_class import Base


class User(Base):
    __tablename__ = "users"

    employee_id = Column(String(100), unique=True, index=True)
    username = Column(String(100), default="")
    email = Column(String(100), unique=True, default="")
    phone = Column(String(100), unique=True, default="")
    hashed_password = Column(String(100))

    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    items = relationship("Item", back_populates="owner")
    blacklists = relationship("Blacklist", back_populates="owner")