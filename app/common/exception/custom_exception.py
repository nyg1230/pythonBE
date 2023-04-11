from app.common.exception.exception_code import ExcpetionCode

class CustomException(Exception):
    def __init__(self, error_code, error_message, status_code):
        self.__error_code       = error_code
        self.__error_message    = error_message
        self.__status_code      = status_code
        
    def __init__(self, error_info: ExcpetionCode):
        self.__error_code       = error_info.get_code()
        self.__error_message    = error_info.get_message()
        self.__status_code      = error_info.get_status()
    
    def get_error_code(self):
        return self.__error_code
    
    def get_error_message(self):
        return self.__error_message
    
    def get_status_code(self):
        return self.__status_code
    
    def get_error_info(self):
        error_info = {
            "statusCode"    : self.get_status_code(),
            "errorCode"     : self.get_error_code(),
            "errorMessage"  : self.get_error_message()
        }
        return error_info
