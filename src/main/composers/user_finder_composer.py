from infra.db.repository.repository_user import UserRepository
from infra.redis_db.repository.repository_redis import RedisRepository
from data.use_cases.user_finder import UserFinderService
from presentation.controllers.user_finder_controller import UserFinderController
from infra.redis_db.settings.connection import RedisConnection


def user_finder_composer():
    conn = RedisConnection()
    repository_redis = RedisRepository(conn.get_connection())
    reposytory = UserRepository()
    use_case = UserFinderService(reposytory, repository_redis)
    controller = UserFinderController(use_case)
    return controller.handle
