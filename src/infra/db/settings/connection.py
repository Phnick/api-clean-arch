from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = f"mysql+mysqlconnector://{
            usuario}:{senha}@{servidor}/{database}"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')
servidor = os.getenv('SERVIDOR')
database = os.getenv('DATABASE')
