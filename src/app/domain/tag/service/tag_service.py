from app.domain.base.service.base_service import BaseService
from app.domain.tag.repository.tag_repository import TagRepository
from app.domain.tag.vo.tag_vo import TagVo

tag_repository = TagRepository()

class TagService(BaseService):
    def __init__(self):
        super().__init__()

    def create_tag(self, obj: dict):
        tag_vo = TagVo().create(**obj)
        tag_repository.create_tag(tag = tag_vo)
        
        return tag_repository.find_by_oid(tag_vo)

    def create_tags(self, tags: list[TagVo]):
        return tag_repository.create_tags(tags = tags)

    def get_tags_by_target_oid(self, target_oid):
        result = tag_repository.get_tags_by_target_oid(target_oid)
        
        tags = []
        
        for data in result:
            tag = TagVo(**data)
            tags.append(tag)

        return tags
    
    def delete_tag(self, json: dict):
        tag = TagVo(**json)
        
        return tag_repository.delete_by_oid(tag)