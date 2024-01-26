from app.domain.base.repository.base_repository import BaseRepository
from app.domain.base.vo.base_vo import BaseVo
from app.common.param.page_vo import PageVo
from app.common.param.order_vo import OrderVo
from app.common.param.where_vo import WhereVo

base_repository = BaseRepository()

class BaseService():
    __test = None

    def __init__(self):
        self.__test = None

    def find_by_oid(self, vo):
        return base_repository.find_by_oid(vo)

    def update(self, vo: BaseVo):
        return base_repository.update(vo)