from presentation.interfaces.controller_interface import ControllerInterface
from domain.use_cases.user_register import UserRegisterServiceInterface
from presentation.http_types.http_request import HttpRequest
from presentation.http_types.http_response import HttpResponse
from schemas.schemas import User, UserSimple

# o arquivo presentation é um intermédio entre as requisições e os casos de uso, importante para deixa o codigo desacoplado, ou seja, nao fica preso ao framework


class UserRegisterController(ControllerInterface):
    def __init__(self, use_case: UserRegisterServiceInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.body["first_name"]
        last_name = http_request.body["last_name"]
        email = http_request.body["email"]
        password = http_request.body["password"]

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        response = self.__use_case.create_user(user)

        # response_model = UserSimple.from_orm(response)

        return HttpResponse(
            status_code=201,
            body=response
        )
