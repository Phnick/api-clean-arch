from security.user_logged import UserLoggedService
from infra.db.repository.repository_user import UserRepository


def get_user_from_token(token: str):
    repository = UserRepository()
    user_logged_service = UserLoggedService(repository)
    user = user_logged_service.get_user_logged(token)
    return user
