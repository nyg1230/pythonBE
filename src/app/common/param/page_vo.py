from app.common.util import common_util

class PageVo():
    __page: int = 0
    __count: int = 20
    __total: int = None

    def __init__(self, obj):
        if (common_util.is_dict(obj) == True):
            self.set(obj)
        
    def get_page(self) -> int: return self.__page
    def set_page(self, page: int = 0): self.__page = page
    
    def get_count(self) -> int: return self.__count
    def set_count(self, count: int = 0): self.__count = count

    def get_total(self) -> int: return self.__total
    def set_total(self, total): self.__total = total

    def get_query(self) -> str:
        return f"OFFSET {self.get_page()} FETCH FIRST {self.get_count()} ROWS ONLY"

    def to_dict(self):
        return {
            "page": self.get_page(),
            "count": self.get_count(),
            "total": self.get_total()
        }

    def set(self, obj: dict):
            for key in obj:
                try:
                    self.__getattribute__(f"set_{key}")(obj[key])
                except:
                    continue
