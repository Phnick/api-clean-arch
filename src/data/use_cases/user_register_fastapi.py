from fastapi import HTTPException, status
from data.interface.repository_user import UserRepositoryInterface
from domain.use_cases.user_register import UserRegisterServiceInterface
from schemas.schemas import User
from typing import Dict
from providers.hash_providers import Hash


class UserRegisterServiceFastapi(UserRegisterServiceInterface):
    '''Aqui eu uso a framewok direto'''

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
        self.hash = Hash()

    def create_user(self, user: User) -> Dict:
        self.__validate_name(user.first_name)
        self.__validate_name(user.last_name)
        self.__validate_email(user.email)
        self.__validate_password(user.password)

        hash_password = self.hash.create_hash(user.password)
        user.password = hash_password

        users = self.user_repository.insert_user(user)

        return users

    @classmethod
    def __validate_name(cls, first_name: str):
        if not first_name.isalpha():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='O campo deve ter a penas letras.')

    @classmethod
    def __validate_email(cls, email: str):
        if not email or "@" not in email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='O campo email é obrigatório e deve ser válido.')

    @classmethod
    def __validate_password(cls, password):
        if not password or len(password) < 6:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='O campo password é obrigatório e deve ter pelo menos 6 caracteres')
