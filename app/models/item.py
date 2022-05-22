from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.base_class import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=False)
    title = Column(String(20), index=True)
    description = Column(String(20), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")