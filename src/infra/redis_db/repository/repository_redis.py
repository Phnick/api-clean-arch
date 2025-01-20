from data.interface.repository_redis import RedisRepositoryInterface
from redis import Redis


class RedisRepository(RedisRepositoryInterface):
    '''Repository Redis'''

    def __init__(self, redis_conn: Redis):
        self.__redis_conn = redis_conn

    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_conn.set(key, value, ex=ex)

    def get(self, key: str):
        value = self.__redis_conn.get(key)
        if value is None:
            return None
        return value.decode("utf-8")

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)
