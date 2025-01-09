from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import mysql.connector
from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv

load_dotenv()


class DatabaseConfig:
    def __init__(self, usuario: str, senha: str, servidor: str, database: str):
        self.usuario = usuario
        self.senha = senha
        self.servidor = servidor
        self.database = database

    def get_database_url(self):
        return f"mysql+mysqlconnector://{self.usuario}:{self.senha}@{self.servidor}/{self.database}"


class DatabaseManager(ABC):
    @abstractmethod
    def criar_bd_se_nao_existe(self):
        raise Exception('create bd if not exist')

    @abstractmethod
    def criar_bd(self):
        raise Exception('create bd')


class MySQLDatabaseManager(DatabaseManager):
    def __init__(self, db_config: DatabaseConfig):
        self.db_config = db_config
        self.engine = create_engine(self.db_config.get_database_url())
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def criar_bd_se_nao_existe(self):
        conn = mysql.connector.connect(
            user=self.db_config.usuario, password=self.db_config.senha, host=self.db_config.servidor)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {
                       self.db_config.database}")
        conn.commit()
        cursor.close()
        conn.close()

    def criar_bd(self):
        self.criar_bd_se_nao_existe()
        self.Base.metadata.create_all(bind=self.engine)

# def get_db(self):
#         db = self.SessionLocal()
#         try:
#             yield db
#         finally:
#             db.close()


usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')
servidor = os.getenv('SERVIDOR')
database = os.getenv('DATABASE')

db_config = DatabaseConfig(usuario, senha, servidor, database)
# esse db_manager vou chamar ele no parametrois de função das minha rotas  db: Session = Depends(db_manager.get_db)
db_manager = MySQLDatabaseManager(db_config)


def get_db():
    db = db_manager.SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_manager.criar_bd()
