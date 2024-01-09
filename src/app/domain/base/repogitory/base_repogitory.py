from app.common.util.connection_util import ConnectionUtil
from app.domain.base.vo.base_vo import BaseVo
from itertools import repeat

class BaseRepogitory():
    __entity = None
    
    def __init__(self, entity: str = None):
        self.__entity = entity

    def get_entity(self) -> str: return self.__entity

    def find_by_oid(self, vo: BaseVo) -> BaseVo:
        oid = BaseVo.get_oid()
        sql = f"SELECT * FROM {vo.get_entity()} WHERE OID = %s"

        return ConnectionUtil.select_one(sql, (oid, ))

    def get_column_data(self, data, columns):
        dataList = []

        for column in columns:
            dataList.append(data.__getattribute__(f"get_{column}")())
            
        return tuple(dataList)

    def insert(self, entity, data, columns):
        values = f"""({", ".join(list(repeat("%s", columns.__len__())))})"""

        sql = f"""
        INSERT INTO {entity} (
            {", ".join(columns)}
        ) VALUES
            {", ".join(values)}
        """
        
        return ConnectionUtil.execute(sql, self.get_column_data(data, columns))

    def multiple_insert(self, entity, datas, columns):
        params = []
        for data in datas:
            params.append(self.get_column_data(data, columns))                

        print(params)
        sql = f"""
        INSERT INTO {entity} (
            {", ".join(columns)}
        ) VALUES %s
        """
        
        return ConnectionUtil.multiple_insert(sql, params)
