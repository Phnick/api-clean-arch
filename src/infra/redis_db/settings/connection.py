from infra.redis_db.settings.connection_options import connection_options
from redis import Redis


class RedisConnection:
    def __init__(self):
        self.__host = connection_options["HOST"]
        self.__port = connection_options["PORT"]
        self.__db = connection_options["BD"]
        self.__connection = None

    def connect(self):
        self.__connection = Redis(
            host=self.__host,
            port=self.__port,
            db=self.__db

        )
        return self.__connection

    def get_connection(self) -> Redis:
        if self.__connection is None:
            self.connect()
        return self.__connection
