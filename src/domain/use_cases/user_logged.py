from abc import ABC, abstractmethod


class UserLoggedServiceInterface(ABC):
    @abstractmethod
    def get_user_logged(self, token: str):
        pass
