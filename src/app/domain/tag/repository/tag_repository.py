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
    
    def get_tags_by_target_oid(self, target_oid):
        columns = ["oid", "tag", "target_type", "target_oid", "created_date"]
        
        sql = f"""
        SELECT
            {", ".join(columns)}
        FROM
            {self.get_entity()}
        WHERE
            TARGET_OID = %s
        """
        
        return ConnectionUtil.execute(sql, (target_oid, ))