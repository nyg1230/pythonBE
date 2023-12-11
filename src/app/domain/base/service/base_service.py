class BaseService():
    __test = None

    def __init__(self):
        self.__test = None
        
    def get_repogiroty(self):
        return self.__repogitory
        
    def find_by_oid(self, oid):
        return self.__repogitory().find_by_oid(oid)