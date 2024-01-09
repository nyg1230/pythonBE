from app.domain.base.vo.base_vo import BaseVo

class UserVo(BaseVo):
    entity = "NMUser"
    __account: str = None
    __pwd: str = None
    __email: str = None
    __created_date = None
    __modified_date = None
    __nickname: str = None
    __sex: str = None
    
    __json = ["pwd", "account", "email", "nickname", "sex"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_account(self): return self.__account
    def set_account(self, account): self.__account = account
        
    def get_pwd(self): return self.__pwd
    def set_pwd(self,pwd): self.__pwd = pwd

    def get_email(self): return self.__email
    def set_email(self, email): self.__email = email
    
    def get_nickname(self): return self.__nickname
    def set_nickname(self, nickname): self.__nickname = nickname
    
    def get_sex(self): return self.__sex
    def set_sex(self, sex): self.__sex = sex

    def check_pw(self, pwd):
        return self.__pwd == pwd
    
    def get_token_info(self):
        p = {
            "account": self.__account,
            "email": self.__email,
            "nickname": self.__nickname,
            "sex": self.__sex
        }

        return p
    
    def to_json(self):
        return super().to_json(self.__json)