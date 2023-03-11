class ErrorInfo:
    def __init__(self, code, message, status = 400):
        self.__code     = code
        self.__message  = message
        self.__status   = status
        
    def get_code(self):
        return self.__code

    def get_message(self):
        return self.__message

    def get_status(self):
        return  self.__status
    