from presentation.http_types.http_response import HttpResponse
from errors.types.http_bad_request import HttpBadRequestError


def handler_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server error",
                "detail": str(error)
            }]
        }
    )
