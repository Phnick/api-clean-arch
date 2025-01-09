from fastapi import Request, APIRouter, status
from fastapi.responses import JSONResponse
from main.adapters.request_adapter import request_adapter
from main.composers.user_register_composer import user_register_composer
from infra.db.settings.connection import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from errors.error_handler import handler_error

router = APIRouter()

#  rota sem a necessidade exclusiva de uma framework


@router.post('/api/v1/register')
async def register(request: Request, db: Session = Depends(get_db)):
    controller = user_register_composer(db)
    try:
        http_response = await request_adapter(request, controller)
    except Exception as exception:
        http_response = handler_error(exception)
    # return http_response.body, http_response.status_code
    return JSONResponse(
        status_code=http_response.status_code,
        content=http_response.body
    )
    # JSONResponse é especifico  da framework, ou seja estou fazendo com que meu htt_reponse retorne confome ela
