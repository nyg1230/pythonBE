from app.common.util.connection_util import ConnectionUtil
from app.domain.base.vo.base_vo import BaseVo
from app.common.param.page_vo import PageVo
from app.common.param.order_vo import OrderVo
from app.common.param.where_vo import WhereVo
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

    def update(self, vo: BaseVo):
        columns = vo.has_columns(vo, False)

        target = []
        values = []
        for col in columns:
            v = vo.get_value(col)
            values.append(v)
            target.append(f"{col} = %s")
        
        sql = f"""
        UPDATE {vo.get_entity()} SET
            {", ".join(target)}
        WHERE
            OID = %s
        """

        values.append(vo.get_oid())
        param = tuple(values)

        return ConnectionUtil.update(sql, param)
    
    def select(self, vo: BaseVo, json: dict, where: WhereVo):
        page = PageVo(json.get("page"))
        sort = OrderVo(vo, json.get("sort"))
        
        sql = f"""
        SELECT
            {", ".join(vo.get_columns())}
        FROM
            {vo.get_entity()}
        {where.get_query()}
        {sort.get_query()}
        {page.get_query()}
        """

        result = ConnectionUtil.execute(sql, where.get_param())
        vo_list = []

        for d in result:
            o = vo(**d)
            vo_list.append(o)
        
        total = self.select_total_count(vo, where)
        page.set_total(total)
        
        return {
            "data": vo_list,
            "page": page.to_dict()
        }
    
    def select_total_count(self, vo: BaseVo, where: WhereVo):
        sql = f"""
        SELECT
            COUNT(1) as count
        FROM
            {vo.get_entity()}
        {where.get_query()}
        """
        
        result = ConnectionUtil.select_one(sql, where.get_param())
        
        return result.get("count")