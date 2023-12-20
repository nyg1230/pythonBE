from enum import Enum

class ExcpetionCode(Enum):
    JWT_EXPIRED_PERIOD = { "code": "jwt_00001", "message": "", "status": 401 }
    JWT_INVALID = { "code": "jwt_00002", "message": "", "status": 401 }
    
    NOT_EXIST_USER = { "code": "u_00001", "message": "", "status": 409 }
    LOGIN_FAIL = { "code": "u_00002", "message": "", "status": 409 }
    DUPLICATE_USER = { "code": "u_00003", "message": "", "status": 400 }
    
    DB_ERROR = { "code": "db_00001", "message": "", "status": 500 }
    CONN_CREATE_ERROR = { "code": "db_00002", "message": "", "status": 500 }
    CONN_CLOSE_ERROR = { "code": "db_00003", "message": "", "status": 500 }
    MANY_RESULTSET = { "code": "db_00004", "message": "", "status": 400 }
    
    def get_code(self): return self.value["code"]
    def get_message(self): return self.value["message"]
    def get_status(self): return self.value["status"]
