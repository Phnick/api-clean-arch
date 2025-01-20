from abc import ABC, abstractmethod


class UserSenderEmailServiceInterface(ABC):
    @abstractmethod
    def send_confirmation_email(self, user_email: str):
        pass
