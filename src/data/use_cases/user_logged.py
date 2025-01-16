from data.interface.repository_user import UserRepositoryInterface
from domain.use_cases.user_logged import UserLoggedServiceInterface
from errors.types.http_bad_request import HttpBadRequestError
from errors.types.http_not_found import HttpNotFoundError
from providers.token_providers import TokenJwt
from jose import JWTError


class UserLoggedService(UserLoggedServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
        self.tokenjwt = TokenJwt()

    def get_user_logged(self, token: str):
        try:
            email = self.tokenjwt.verify_access_token(token)
        except JWTError:
            raise HttpBadRequestError('Token inválido')

        if not email:
            raise HttpNotFoundError('Email não encontrado')

        user = self.user_repository.get_email(email)
        if not user:
            raise HttpNotFoundError('Usuário não encotrado')

        return user
