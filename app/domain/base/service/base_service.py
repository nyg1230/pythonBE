from app.domain.base.repogitory.base_repogitory import BaseRepogitory

class BaseService():
    __repogitory = BaseRepogitory
    def __init__(self, repo):
        self.__repogitory = repo
        
    def find_by_oid(self, oid):
        return self.__repogitory().find_by_oid(oid)