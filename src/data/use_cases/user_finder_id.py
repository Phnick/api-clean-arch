from data.interface.repository_user import UserRepositoryInterface
from domain.use_cases.user_finder_id import UserFinderIdServiceInterface
from errors.types.http_not_found import HttpNotFoundError
from errors.types.http_bad_request import HttpBadRequestError
from schemas.schemas import UserSimple
from typing import Dict


class UserFinderId(UserFinderIdServiceInterface):
    '''Use case UserFindId'''

    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository

    def finder_id(self, id: int):
        self.__validate_id(id)
        user = self.__search_user(id)
        response = self.__format_response(user)
        return response

    @classmethod
    def __validate_id(cls, id: int):
        # if not isinstance(id, int):
        try:
            id = int(id)
        except ValueError:
            raise HttpBadRequestError('O id deve ser um número inteiro')
        return id

    def __search_user(self, id: int):
        user = self.__user_repository.select_user_id(id)
        if not user:
            raise HttpNotFoundError('Esse Id não exite')
        return user

    @classmethod
    def __format_response(cls, user: UserSimple):
        '''Response Model'''
        response = {
            "type": "User",
            "atributes": {
                "id": user.id,
                "first_name": user.first_name,
                "email": user.email

            }
        }
        return response
