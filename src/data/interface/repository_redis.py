from abc import ABC, abstractmethod


class RedisRepositoryInterface(ABC):
    '''RepositoryRedis interface'''

    @abstractmethod
    def insert_ex(self, key: str, value: any, ex: int):
        pass

    @abstractmethod
    def get(self, key: str):
        pass

    def insert(self, key: str, value: any):
        pass
