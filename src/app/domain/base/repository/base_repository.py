from app.common.util.connection_util import ConnectionUtil
from app.domain.base.vo.base_vo import BaseVo
from app.common.param.page_vo import PageVo
from itertools import repeat


class BaseRepository():
    __entity = None
    
    def __init__(self, entity: str = None):
        self.__entity = entity

    def get_entity(self) -> str: return self.__entity

    def find_by_oid(self, vo: BaseVo) -> BaseVo:
        oid = BaseVo.get_oid()
        sql = f"SELECT * FROM {vo.get_entity()} WHERE OID = %s"

        return ConnectionUtil.select_one(sql, (oid, ))

    def get_column_data(self, data: BaseVo, columns: list[str]):
        dataList = []

        for column in columns:
            dataList.append(data.__getattribute__(f"get_{column}")())
            
        return tuple(dataList)

    def insert(self, data: BaseVo, columns: list[str]):
        values = f"""({", ".join(list(repeat("%s", columns.__len__())))})"""
        sql = f"""
        INSERT INTO {self.get_entity()} (
            {", ".join(columns)}
        ) VALUES
            {", ".join(values)}
        """
        
        return ConnectionUtil.execute(sql, self.get_column_data(data, columns))

    def multiple_insert(self, datas: list[BaseVo], columns = list[str]):
        params = []
        for data in datas:
            params.append(self.get_column_data(data, columns))                

        sql = f"""
        INSERT INTO {self.get_entity()} (
            {", ".join(columns)}
        ) VALUES %s
        """
        
        return ConnectionUtil.multiple_insert(sql, params)
