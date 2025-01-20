class HttpEmailSendError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'EmailSendError'
        self.status_code = 500
