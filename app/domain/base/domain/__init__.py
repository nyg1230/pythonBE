class BaseObject:
    def __init__(self, param: dict):
        self.__oid: int  = param["oid"]
        self.__name: str = param["name"]

    def get_oid(self): return self.__oid
    def set_oid(self, oid: int): self.__oid = oid
    
    def get_name(self): return self.__name
    def set_name(self, name: str): self.__name = name