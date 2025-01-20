from presentation.http_types.http_response import HttpResponse
from errors.types.http_bad_request import HttpBadRequestError
from errors.types.http_not_found import HttpNotFoundError
from errors.types.http_email_send_error import HttpEmailSendError


def handler_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpEmailSendError)):
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
