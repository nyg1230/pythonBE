class BaseService():
    __test = None

    def __init__(self):
        self.__test = None
        
    def get_reposiroty(self):
        return self.__repository
        
    def find_by_oid(self, oid):
        return self.__repository().find_by_oid(oid)