from enum import Enum

class ExcpetionCode(Enum):
    def get_code(self): return self.value["code"]
    def get_message(self): return self.value["message"]
    def get_status(self): return self.value["status"]
