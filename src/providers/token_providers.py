from datetime import datetime, timedelta
from jose import jwt
from typing import Dict
import os


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
EXPIRES_IN_MINUTES = 60


class TokenJwt:
    @staticmethod
    def creat_acces_token(data: Dict):
        '''Cria um token JWT com dados e data de expiração'''
        dados = data.copy()
        expires = datetime.utcnow()+timedelta(minutes=EXPIRES_IN_MINUTES)

        dados.update({'exp': expires})
        token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
        return token_jwt

    @staticmethod
    def verify_access_token(token: str):
        '''Verifica o token JWT e retorna o valor do 'sub' ou levanta exceções em caso de erro'''
        carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return carga.get('sub')
