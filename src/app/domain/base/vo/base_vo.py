from app.domain.base.repogitory.base_repogitory import BaseRepogitory

class BaseService():
    __oid = ""
    def __init__(self):
        print("base_vo")

    def get_oid(self):
        return self.__oid

    def set_oid(self, oid):
        self.__oid = oid