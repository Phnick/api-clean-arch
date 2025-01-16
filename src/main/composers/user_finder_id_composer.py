from infra.db.repository.repository_user import UserRepository
from data.use_cases.user_finder_id import UserFinderId
from presentation.controllers.user_finder_id_controller import UserFinderIdController


def user_finder_id_composer():
    repository = UserRepository()
    use_case = UserFinderId(repository)
    controller = UserFinderIdController(use_case)

    return controller.handle
