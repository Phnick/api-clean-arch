from infra.db.repository.repository_user import UserRepository
from data.use_cases.user_register import UserRegisterService
from presentation.controllers.user_register_controller import UserRegisterController


def user_register_composer():
    repository = UserRepository()
    use_case = UserRegisterService(repository)
    controller = UserRegisterController(use_case)

    return controller.handle
