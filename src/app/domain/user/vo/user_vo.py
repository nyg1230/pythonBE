from app.domain.base.vo.base_vo import BaseVo

class UserVo(BaseVo):
    __account = None
    __pwd = None
    __email = None
    __created_date = None
    __modified_date = None
    __nickname = None
    __sex = None

    def __init__(self, *args, **kwargs):
        super().__init__("NMUser", *args, **kwargs)
    
    def get_account(self): return self.__account
    def set_account(self, account): self.__account = account
        
    def get_pwd(self): return self.__pwd
    def set_pwd(self,pwd): self.__pwd = pwd

    def get_email(self): return self.__email
    def set_email(self, email): self.__email = email

    def get_created_date(self): return self.__created_date
    def set_created_date(self, date): self.__created_date = date
    
    def get_modified_date(self): return self.__modified_date
    def set_modified_date(self, date): self.__modified_date = date
    
    def get_nickname(self): return self.__nickname
    def set_nickname(self, nickname): self.__nickname = nickname
    
    def get_sex(self): return self.__sex
    def set_sex(self, sex): self.__sex = sex

    def check_pw(self, pwd):
        return self.__pwd == pwd
    
    def get_token_info(self):
        p = {
            "account": self.__account,
            "email": self.__email
        }

        return p
    
    def to_json(self):
        list = ["oid", "pwd", "email", "created_date", "modified_date", "nickname", "sex"]
        return super().to_json(list)