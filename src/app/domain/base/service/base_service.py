from app.domain.base.repository.base_repository import BaseRepository
from app.domain.base.vo.base_vo import BaseVo

base_repository = BaseRepository()

class BaseService():
    __test = None

    def __init__(self):
        self.__test = None

    def find_by_oid(self, vo):
        return base_repository.find_by_oid(vo)
    
    def update(self, vo: BaseVo):
        return base_repository.update(vo)