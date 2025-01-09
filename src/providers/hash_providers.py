from passlib.context import CryptContext


pwd_context = CryptContext(schemes='bcrypt')


class Hash:
    def __init__(self):
        self.pwd_context = pwd_context

    def create_hash(self, text):
        return self.pwd_context.hash(text)

    def check_hash(self, text, hash):
        return pwd_context.verify(text, hash)
