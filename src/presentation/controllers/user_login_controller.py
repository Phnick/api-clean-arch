from presentation.interfaces.controller_interface import ControllerInterface
from domain.use_cases.user_login import UserLoginSericeInterface
from presentation.http_types.http_request import HttpRequest
from presentation.http_types.http_response import HttpResponse


class UserLoginController(ControllerInterface):
    def __init__(self, use_case: UserLoginSericeInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        email = http_request.body["email"]
        password = http_request.body["password"]

        response = self.__use_case.user_login(email, password)

        return HttpResponse(
            status_code=200,
            body=response
        )
