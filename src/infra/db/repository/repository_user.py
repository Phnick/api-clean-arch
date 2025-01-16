from sqlalchemy.orm import Session
from sqlalchemy import select
from infra.db.settings.connection import DBConnectionHandler
from schemas.schemas import User, UserSimple
from infra.db.entities import models
from typing import List
from data.interface.repository_user import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    '''Repository User'''

    @classmethod
    def insert_user(cls, user: User):
        with DBConnectionHandler() as databse:
            db_user = models.RegisterUser(first_name=user.first_name,
                                          last_name=user.last_name,
                                          email=user.email,
                                          password=user.password)

            databse.session.add(db_user)
            databse.session.commit()
            databse.session.refresh(db_user)
            return db_user

    @classmethod
    def select_user(cls, first_name: str):
        with DBConnectionHandler() as databse:
            db_user = databse.session.query(models.RegisterUser).filter(
                models.RegisterUser.first_name == first_name).all()

            return db_user

    @classmethod
    def select_user_id(cls, id: int):
        with DBConnectionHandler() as databse:
            db_user = databse.session.query(models.RegisterUser).filter(
                models.RegisterUser.id == id).scalar()
            return db_user

    @classmethod
    def get_email(cls, email: str):
        with DBConnectionHandler() as databse:
            db_user = databse.session.query(models.RegisterUser).filter(
                models.RegisterUser.email == email).first()
            return db_user
