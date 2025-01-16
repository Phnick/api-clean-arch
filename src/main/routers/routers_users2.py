from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from main.adapters.request_adapter import request_adapter
from main.composers.user_register_composer import user_register_composer
from main.composers.user_finder_composer import user_finder_composer
from main.composers.user_finder_id_composer import user_finder_id_composer
from main.composers.user_login_composer import user_login_composer
from errors.error_handler import handler_error

router = APIRouter()

#  rota sem a necessidade exclusiva de uma framework


@router.post('/api/v1/user/register')
async def register(request: Request):
    controller = user_register_composer()
    try:
        http_response = await request_adapter(request, controller)
    except Exception as exception:
        http_response = handler_error(exception)
    return JSONResponse(
        status_code=http_response.status_code,
        content=http_response.body
    )


@router.get('/api/v1/user/finder')
async def find_user(request: Request):
    controller = user_finder_composer()
    try:
        http_response = await request_adapter(request, controller)
    except Exception as exception:
        http_response = handler_error(exception)
    return JSONResponse(
        status_code=http_response.status_code,
        content=http_response.body
    )


@router.get('/api/v1/user/finder/{id}')
async def find_user_id(request: Request):

    controler = user_finder_id_composer()
    try:
        http_response = await request_adapter(request, controler)
    except Exception as exception:
        http_response = handler_error(exception)
    return JSONResponse(
        status_code=http_response.status_code,
        content=http_response.body
    )


@router.post('/api/v1/user/login')
async def login_user(request: Request):
    controler = user_login_composer()
    try:
        http_response = await request_adapter(request, controler)
    except Exception as exception:
        http_response = handler_error(exception)
    return JSONResponse(
        status_code=http_response.status_code,
        content=http_response.body
    )
