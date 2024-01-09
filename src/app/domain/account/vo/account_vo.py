from app.domain.base.vo.base_vo import BaseVo

class AccountVo(BaseVo):
    entity = "NMAccountBook"
    __user_oid: str = None
    __target_date = None
    __memo: str = None
    __amount: int = None
    __order_num: int = None
    __type: str = None
    __is_delete: bool = None
    
    __json = ["oid"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_user_oid(self) -> str: return  self.__user_oid
    def set_user_oid(self, user_oid): self.__user_oid = user_oid
    
    def get_target_date(self): return self.__target_date
    def set_target_date(self, date): self.__target_date = date
    
    def get_memo(self) -> str: return self.__memo
    def set_memo(self, memo): self.__memo = memo
    
    def get_amount(self) -> int: return self.__amount
    def set_amount(self, amount): self.__amount = amount
    
    def get_type(self) -> str: return self.__type
    def set_type(self, type): self.__type = type

    def get_order_num(self) -> int: return self.__order_num
    def set_order_num(self, num): self.__order_num = num
    
    def get_is_delete(self) -> bool: return self.__is_delete
    def set_is_delete(self, bool): self.__is_delete = bool
    
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