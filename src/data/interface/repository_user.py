from abc import ABC, abstractmethod
from schemas.schemas import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, user: User):
        pass

    @abstractmethod
    def select_user(self, first_name: str):
        pass
