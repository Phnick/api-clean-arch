from abc import ABC, abstractmethod
from presentation.http_types.http_request import HttpRequest
from presentation.http_types.http_response import HttpResponse

# no caso de clean architecture os controllers sao usados para interagir com os casos de uso


class ControllerInterface(ABC):
    @abstractmethod
    # gerenciar
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
