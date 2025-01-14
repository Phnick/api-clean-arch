from abc import ABC, abstractmethod


class UserFinderServiceInterface(ABC):
    @abstractmethod
    def find(self, first_name: str):
        pass
