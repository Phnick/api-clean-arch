from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.schemas import User, UserSimple
from infra.db.entities import models
from typing import List
from data.interface.repository_user import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    '''Repository User'''

    def __init__(self, db: Session):
        self.db = db

    def insert_user(self, user: User):
        db_user = models.RegisterUser(first_name=user.first_name,
                                      last_name=user.last_name,
                                      email=user.email,
                                      password=user.password)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def select_user(self, first_name: str):
        db_user = self.db.query(models.RegisterUser).filter(
            models.RegisterUser.first_name == first_name).all()

        return db_user

    def select_user_id(self, id: int):
        db_user = self.db.query(models.RegisterUser).filter(
            models.RegisterUser.id == id).scalar()
        return db_user
