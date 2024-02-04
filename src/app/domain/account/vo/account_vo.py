from app.domain.base.vo.base_vo import BaseVo
from app.domain.tag.vo.tag_vo import TagVo

class AccountVo(BaseVo):
    entity = "NMAccountBook"
    columns = ["user_oid", "target_date", "history", "memo", "amount", "order_num", "category"]
    __user_oid: str = None
    __target_date = None
    __history: str = None
    __memo: str = None
    __amount: int = None
    __order_num: int = None
    __category: str = None
    __is_delete: bool = None
    __tags: list[TagVo] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_user_oid(self) -> str: return  self.__user_oid
    def set_user_oid(self, user_oid): self.__user_oid = user_oid
    
    def get_target_date(self): return self.__target_date
    def set_target_date(self, date): self.__target_date = date

    def get_history(self) -> str: return self.__history
    def set_history(self, history): self.__history = history

    def get_memo(self) -> str: return self.__memo
    def set_memo(self, memo): self.__memo = memo
    
    def get_amount(self) -> int: return self.__amount
    def set_amount(self, amount): self.__amount = amount

    def get_category(self) -> str: return self.__category
    def set_category(self, category): self.__category = category

    def get_order_num(self) -> int: return self.__order_num
    def set_order_num(self, num): self.__order_num = num
    
    def get_is_delete(self) -> bool: return self.__is_delete
    def set_is_delete(self, bool): self.__is_delete = bool
    
    def get_tags(self) -> list[TagVo]: return self.__tags
    def set_tags(self, tags): self.__tags = tags
    
    def to_dict(self):
        d = super().to_dict()
        
        tags = self.get_tags()
        if (tags is not None):
            tag_list = []
            for tag in tags:
                tag_list.append(tag.to_dict())

            d.__setitem__("tags", tag_list)
        return d