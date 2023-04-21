from enum import Enum

class ExcpetionCode(Enum):
    JWT_EXPIRED_PERIOD = { "code": "token_00001", "message": "", "status": 401 }
    JWT_INVALID = { "code": "token_00002", "message": "", "status": 401 }
    
    def get_code(self): return self.value["code"]
    def get_message(self): return self.value["message"]
    def get_status(self): return self.value["status"]
