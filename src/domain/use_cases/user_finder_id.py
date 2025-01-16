from abc import ABC, abstractmethod


class UserFinderIdServiceInterface(ABC):
    @abstractmethod
    def finder_id(self, id: int):
        pass
