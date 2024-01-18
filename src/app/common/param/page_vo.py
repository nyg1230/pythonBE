class PageVo():
    __page: int = 0
    __count: int = 20
    
    def __init__(self, *args, **kwargs):
        self.set(kwargs)
        
    def get_page(self) -> int: return self.__page
    def set_page(self, page: int = 0): self.__page = page
    
    def get_count(self) -> int: return self.__count
    def set_count(self, count: int = 0): self.__count = count

    def get_query(self) -> str:
        return f"OFFSET {self.get_page()} FETCH FIRST {self.get_count()} ROWS ONLY"

    def set(self, obj: dict):
            for key in obj:
                try:
                    self.__getattribute__(f"set_{key}")(obj[key])
                except:
                    continue
