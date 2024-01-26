from enum import Enum

from app.domain.base.vo.base_vo import BaseVo
from app.common.util import common_util

class order(Enum):
    ASC = "ASC"
    DESC = "DESC"

class OrderVo:
    __vo = None
    __orders = []

    def __init__(self, vo: BaseVo, arr: list):
        self.__vo = vo
        self.set(arr)
        
    def __get_order(self, sort):
        is_same = common_util.case_sensitive(sort, order.DESC.value)

        return order.DESC.value if is_same else order.ASC.value

    def set(self, arr: dict):
        self.__orders = []

        for d in arr:
            k, v = d
            if (self.__vo.has_column(k)):
                self.__orders.append(f"{k} {self.__get_order(v)}")
        
    def get_query(self):
        query = ""
        
        if self.__orders.__len__() > 0:
            query = f"""ORDER BY {", ".join(self.__orders)}"""

        return query