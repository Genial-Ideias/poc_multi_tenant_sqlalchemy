from sqlalchemy import Column, String, Integer, Boolean

from src.config.database import TenantBase


class User(TenantBase):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    is_active = Column(Boolean, default=True)
