from abc import ABC, abstractmethod


class UserLoginSericeInterface(ABC):
    @abstractmethod
    def user_login(email: str, password: str):
        pass
