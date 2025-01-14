from presentation.http_types.http_response import HttpResponse
from fastapi.responses import JSONResponse
from presentation.http_types.http_request import HttpRequest
from fastapi import Request as RequestFastApi
from typing import Callable


# vai ser o limite do framewok, ou seja tirei tudo que eu preciso da framework e colocando no htt_request
# O adaptador pega a requisição da framework (no caso, FastAPI) e adapta ela para o formato que o controlador entende.

async def request_adapter(request: RequestFastApi, controller: Callable) -> HttpResponse:
    try:
        body = await request.json()
    except ValueError:
        body = None
    # Converte o `request` da framework (FastAPI) para um formato genérico
    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url,


    )

    http_response = controller(http_request)

    return http_response
