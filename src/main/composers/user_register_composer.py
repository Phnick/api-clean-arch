from infra.db.repository.repository_user import UserRepository
from data.use_cases.user_register import UserRegisterService
from presentation.controllers.user_register_controller import UserRegisterController
from sqlalchemy.orm import Session
from infra.db.settings.connection import get_db
from fastapi import Depends

# aqui sera juntado tudo,O composer é responsável por "montar" todas as dependências necessárias para o controlador funcionar. Ele cria o repositório, o caso de uso, e o controlador. No final, ele retorna o controlador pronto para ser usado.


def user_register_composer(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    use_case = UserRegisterService(repository)
    controller = UserRegisterController(use_case)

    return controller.handle
