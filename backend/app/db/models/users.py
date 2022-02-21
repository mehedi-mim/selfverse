from sqlalchemy import Boolean, Column, Integer, String, Text
from app.db.session import Base
from app.db.schemas import Status
from .common import CommonBase


class User(Base, CommonBase):
    __tablename__ = "user"

    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    address = Column(Text, nullable=True)
    status = Column(Integer, nullable=True, default=Status.ACTIVE.value)
    phone = Column(String, nullable=True)
    note = Column(Text, nullable=True)

