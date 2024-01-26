from app.domain.base.vo.base_vo import BaseVo

class WhereVo:
    __where = None
    __param = ()
    
    def get_query(self, has_where: bool = False) -> str:
        query = ""
        
        if self.__where == None:
            query = ""
        else:
            query = "WHERE " if has_where else ""
            query = f"{query}{self.__where}"
        
        return query

    def set_where(self, where: str = None): self.__where = where
    
    def get_param(self) -> tuple: self.__param
    def set_param(self, param: tuple = ()): self.__param = param
    