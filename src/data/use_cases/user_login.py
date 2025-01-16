from domain.use_cases.user_login import UserLoginSericeInterface
from data.interface.repository_user import UserRepositoryInterface
from errors.types.http_not_found import HttpNotFoundError
from errors.types.http_bad_request import HttpBadRequestError
from providers.token_providers import TokenJwt
from providers.hash_providers import Hash
from schemas.schemas import LoginSucces


class UserLoginService(UserLoginSericeInterface):
    def __init__(self, user_repositoty: UserRepositoryInterface):
        self.user_repository = user_repositoty
        self.tokenjwt = TokenJwt()
        self.hash = Hash()

    def user_login(self, email: str, password: str):
        self.__validate_email(email)
        self.__validate_password(password)

        user = self.__get_user(email)

        if not self.hash.check_hash(password, user.password):
            raise HttpNotFoundError('Senha ou email incorretos')

        token = self.tokenjwt.creat_acces_token({'sub': user.email})
        login_succes = LoginSucces(user=user, token=token)
        return self.__format_response(login_succes)

    @classmethod
    def __validate_email(cls, email: str):
        if not email or "@" not in email:
            raise HttpBadRequestError(
                'O campo email é obrigatório e deve ser válido.')

    @classmethod
    def __validate_password(cls, password):
        if not password or len(password) < 6:
            raise HttpBadRequestError(
                'O campo password é obrigatório e deve ter pelo menos 6 caracteres')

    def __get_user(self, email: str):
        user = self.user_repository.get_email(email)
        if not user:
            raise HttpNotFoundError('Email não cadastrado')
        return user

    @classmethod
    def __format_response(cls, user: LoginSucces):
        '''Respose model'''
        response = {
            "Type": "Login",
            "attributes": {
                "user": {
                    "id": user.user.id,
                    "first_name": user.user.first_name,
                    "email": user.user.email
                },
                "token": user.token

            }
        }
        return response
