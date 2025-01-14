from infra.db.repository.repository_user import UserRepository
from data.use_cases.user_finder import UserFinderService
from presentation.controllers.user_finder_controller import UserFinderController
from sqlalchemy.orm import Session
from infra.db.settings.connection import get_db
from fastapi import Depends


def user_finder_composer(db: Session = Depends(get_db)):
    reposytory = UserRepository(db)
    use_case = UserFinderService(reposytory)
    controller = UserFinderController(use_case)
    return controller.handle
