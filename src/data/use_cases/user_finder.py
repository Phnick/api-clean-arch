from domain.use_cases.user_finder import UserFinderServiceInterface
from data.interface.repository_user import UserRepositoryInterface
from errors.types.http_bad_request import HttpBadRequestError
from errors.types.http_not_found import HttpNotFoundError
from domain.models.user_models import User
from typing import List, Dict
from schemas.schemas import UserSimple


class UserFinderService(UserFinderServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository

    def find(self, first_name: str):
        self.__validate_name(first_name)
        users = self.__search_user(first_name)
        response = self.__format_response(users)
        return response

    @classmethod
    def __validate_name(cls, firts_name: str):
        if not firts_name.isalpha():
            raise HttpBadRequestError('o nome deve ter a penas letras')

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
