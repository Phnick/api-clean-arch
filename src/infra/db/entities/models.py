# from infra.db.settings.connection import db_manager
from infra.db.settings.base import Base
from sqlalchemy import Column, String, Integer


class RegisterUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(300))
    password = Column(String(250))
