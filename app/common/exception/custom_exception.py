class CustomException(Exception):
    def __init__(self, error_code, error_message, status_code):
        self.__error_code       = error_code
        self.__error_message    = error_message
        self.__status_code      = status_code
    
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