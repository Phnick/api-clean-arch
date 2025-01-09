from sqlalchemy.orm import Session
from schemas.schemas import User
from infra.db.entities import models
from data.interface.repository_user import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
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
