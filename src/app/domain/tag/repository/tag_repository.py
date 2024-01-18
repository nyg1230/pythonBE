from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.tag.vo.tag_vo import TagVo

class TagRepository(BaseRepository):
    def __init__(self):
        super().__init__(TagVo.entity)
        
    def create_tag(self, tag: TagVo):
        columns = ["oid", "tag", "target_type", "target_oid"]
        return self.insert(data = tag, columns = columns)
    
    def create_tags(self, tags: list[TagVo]):
        columns = ["oid", "tag", "target_type", "target_oid"]
        return self.multiple_insert(datas = tags, columns = columns)