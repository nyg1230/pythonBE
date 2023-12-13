from app.common.util.connection_util import ConnectionUtil
from app.domain.base.vo.base_vo import BaseVo

class BaseRepogitory():
    __entity = None
    
    def __init__(self, entity):
        self.__entity = entity
        
    def get_entity(self):
        return self.__entity

    def find_by_oid(self, vo: BaseVo):
        oid = BaseVo.get_oid()
        sql = f"SELECT * FROM {self.get_entity()} WHERE OID = %s"

        return ConnectionUtil.select_one(sql, (oid, ))
