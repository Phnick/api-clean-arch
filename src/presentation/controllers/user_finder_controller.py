from presentation.interfaces.controller_interface import ControllerInterface
from domain.use_cases.user_finder import UserFinderServiceInterface
from presentation.http_types.http_request import HttpRequest
from presentation.http_types.http_response import HttpResponse


class UserFinderController(ControllerInterface):
    def __init__(self, use_case: UserFinderServiceInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]

        response = self.__use_case.find(first_name)

        return HttpResponse(
            status_code=200,
            body=response

        )
