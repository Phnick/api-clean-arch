from infra.db.repository.repository_user import UserRepository
from data.use_cases.user_finder_id import UserFinderId
from presentation.controllers.user_finder_id_controller import UserFinderIdController
from sqlalchemy.orm import Session
from infra.db.settings.connection import get_db
from fastapi import Depends


def user_finder_id_composer(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    use_case = UserFinderId(repository)
    controller = UserFinderIdController(use_case)

    return controller.handle
