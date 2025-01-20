from data.use_cases.user_sender_email import UserSenderEmailService
from errors.types.http_email_send_error import HttpEmailSendError
import os
from celery import Celery
from dotenv import load_dotenv
load_dotenv()

app = Celery('task', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    accept_content=['json'],
    task_serializer='json',
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    worker_pool='solo',
    result_expires=600  # Definir o pool como solo no Windows
)


@app.task
def send_email_task(user_email: str):
    sender_email = os.getenv('FROM_EMAIL')
    sender_password = os.getenv('SMTP_PASSWORD')
    if not sender_email or not sender_password:
        raise HttpEmailSendError(
            "As credenciais de e-mail não foram configuradas corretamente.")

    email_service = UserSenderEmailService(sender_email, sender_password)
    try:
        email_service.send_confirmation_email(user_email)
    except Exception as e:
        raise HttpEmailSendError(
            f"Erro ao enviar email para {user_email}: {e}")
