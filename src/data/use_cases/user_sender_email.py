import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from errors.types.http_email_send_error import HttpEmailSendError
import os


class UserSenderEmailService:
    def __init__(self, sender_email: str, sender_password: str):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_confirmation_email(self, user_email: str):
        msg = self.create_message(user_email)
        self.connect_smtp(msg, user_email)

    def connect_smtp(self, msg: MIMEMultipart, user_email: str):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                text = msg.as_string()
                server.sendmail(self.sender_email, user_email, text)
        except Exception as e:
            raise HttpEmailSendError(f"Erro ao enviar email: {e}")

    def create_message(self, user_email: str) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = user_email
        msg['Subject'] = 'Confirmação de Cadastro'
        body = 'Obrigado por se cadastrar! Seu cadastro foi realizado com sucesso.'
        msg.attach(MIMEText(body, 'plain'))
        return msg