from domain.use_cases.user_finder import UserFinderServiceInterface
from data.interface.repository_user import UserRepositoryInterface
from errors.types.http_bad_request import HttpBadRequestError
from errors.types.http_not_found import HttpNotFoundError
from domain.models.user_models import User
from typing import List, Dict
from schemas.schemas import UserSimple
from data.interface.repository_redis import RedisRepositoryInterface


class UserFinderService(UserFinderServiceInterface):
    '''User Finder Service '''

    def __init__(self, user_repository: UserRepositoryInterface, redis_repository: RedisRepositoryInterface):
        self.__user_repository = user_repository
        self.__redis_repository = redis_repository

    def find(self, first_name: str):
        self.__validate_name(first_name)
        users = self.search_user_redis(first_name)
        if not users:
            users = self.__search_user(first_name)
        response = self.__format_response(users)
        return response

    @classmethod
    def __validate_name(cls, firts_name: str):
        if not firts_name.isalpha():
            raise HttpBadRequestError('o nome deve ter a penas letras')

    def search_user_redis(self, first_name: str):
        '''Busca o first_name no Redis'''

        redis_key = f"user:{first_name}"
        users_redis = self.__redis_repository.get(first_name)
        if users_redis:
            return users_redis
        else:
            users_mysql = self.__user_repository.select_user(first_name)
            if users_mysql:
                self.__redis_repository.insert_ex(
                    redis_key, 'found', ex=50)
        return users_mysql

    def __search_user(self, first_name: str):
        users = self.__user_repository.select_user(first_name)
        if not users:
            raise HttpNotFoundError('Nome não encontrado')

        return users

    @classmethod
    def __format_response(cls, users: List[UserSimple]) -> Dict:
        '''Response model'''
        atributes = []
        for user in users:
            atributes.append(
                {
                    "id": user.id,
                    "first_name": user.first_name,
                    "email": user.email

                }
            )
        response = {
            "type": "Users",
            "count": len(users),
            "attributes": atributes
        }
        return response
