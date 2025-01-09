from abc import ABC, abstractmethod
from schemas.schemas import User
from typing import Dict

# aqui vao ficar as interfaces dos casos de uso


class UserRegisterServiceInterface(ABC):
    @abstractmethod
    def create_user(self, user: User) -> Dict:
        pass
