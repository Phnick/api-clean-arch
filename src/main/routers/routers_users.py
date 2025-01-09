from fastapi import APIRouter, status, Depends
from schemas.schemas import User, UserSimple
from infra.db.settings.connection import get_db
from data.use_cases.user_register import UserRegisterService
from infra.db.repository.repository_user import UserRepository
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/sigup', status_code=status.HTTP_201_CREATED, response_model=UserSimple)
def create_user(user: User, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserRegisterService(user_repository)
    return user_service.create_user(user)
