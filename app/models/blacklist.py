from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.base_class import Base

class Blacklist(Base):
    __tablename__ = "blacklists"

    token = Column(String(100))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="blacklists")