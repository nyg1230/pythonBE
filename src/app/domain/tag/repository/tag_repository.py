from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.tag.vo.tag_vo import TagVo

class TagRepository(BaseRepository):
    def __init__(self):
        super().__init__(TagVo.entity)