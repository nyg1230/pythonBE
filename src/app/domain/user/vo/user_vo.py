from app.domain.base.vo.base_vo import BaseVo

class UserVo(BaseVo):
    __table = "NMUser"
    __account = None
    __pw = None
    __email = None

    def __init__(self):
        super().__init__()
    
    def get_account(self):
        return self.__account
    
    def set_account(self, account):
        self.__account = account
        
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def check_pw(self, pw):
        return self.__pw == pw
    
    def get_token_info(self):
        p = {
            "account": self.__account,
            "email": self.__email
        }

        return p