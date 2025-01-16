from data.use_cases.user_logged import UserLoggedService
from infra.db.repository.repository_user import UserRepository
from infra.db.settings.connection import get_db


def get_user_from_token(token: str):
    db = get_db()
    repository = UserRepository(db)
    user_logged_service = UserLoggedService(repository)
    user = user_logged_service.get_user_logged(token)
    return user
