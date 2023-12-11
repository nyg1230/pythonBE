from enum import Enum

class ExcpetionCode(Enum):
    JWT_EXPIRED_PERIOD = { "code": "jwt_00001", "message": "", "status": 401 }
    JWT_INVALID = { "code": "jwt_00002", "message": "", "status": 401 }
    
    NOT_EXIST_USER = { "code": "u_00001", "message": "", "status": 409 }
    LOGIN_FAIL = { "code": "u_00002", "message":"", "status": 409 }
    
    def get_code(self): return self.value["code"]
    def get_message(self): return self.value["message"]
    def get_status(self): return self.value["status"]
