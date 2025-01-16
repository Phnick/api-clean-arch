from presentation.interfaces.controller_interface import ControllerInterface
from domain.use_cases.user_finder_id import UserFinderIdServiceInterface
from presentation.http_types.http_request import HttpRequest
from presentation.http_types.http_response import HttpResponse


class UserFinderIdController(ControllerInterface):
    def __init__(self, use_case: UserFinderIdServiceInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.path_params["id"]
        response = self.use_case.finder_id(id)

        return HttpResponse(
            status_code=200,
            body=response
        )
