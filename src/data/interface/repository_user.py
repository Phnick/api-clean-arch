from abc import ABC, abstractmethod
from schemas.schemas import User


class UserRepositoryInterface(ABC):
    '''Interface repository user'''
    @abstractmethod
    def insert_user(self, user: User):
        pass

    @abstractmethod
    def select_user(self, first_name: str):
        pass

    @abstractmethod
    def select_user_id(self, id: int):
        pass
