from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship

from ..db.base_class import Base

class User(Base):
    """
    id(PK), created_at, updated_at cols는
    Base 에서 상속.
    """
    # id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, nullable=False, unique=True, index=True)
    username = Column(String(32), default="")
    email = Column(String(32), unique=True, default="")

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    hashed_password = Column(String(100))

    # items = relationship("Item", back_populates="owner")
