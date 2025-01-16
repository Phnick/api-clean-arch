from infra.db.repository.repository_user import UserRepository
from data.use_cases.user_finder import UserFinderService
from presentation.controllers.user_finder_controller import UserFinderController


def user_finder_composer():
    reposytory = UserRepository()
    use_case = UserFinderService(reposytory)
    controller = UserFinderController(use_case)
    return controller.handle
