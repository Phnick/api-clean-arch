from fastapi import APIRouter, status, Depends
from schemas.schemas import User, UserSimple
from data.use_cases.user_register_fastapi import UserRegisterServiceFastapi
from infra.db.repository.repository_user import UserRepository


router = APIRouter()


@router.post('/api/sigup', status_code=status.HTTP_201_CREATED, response_model=UserSimple)
def create_user(user: User):
    user_repository = UserRepository()
    user_service = UserRegisterServiceFastapi(user_repository)
    return user_service.create_user(user)
