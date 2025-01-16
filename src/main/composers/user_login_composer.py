from infra.db.repository.repository_user import UserRepository
from data.use_cases.user_login import UserLoginService
from presentation.controllers.user_login_controller import UserLoginController


def user_login_composer():
    userRepository = UserRepository()
    use_case = UserLoginService(userRepository)
    controller = UserLoginController(use_case)

    return controller.handle
