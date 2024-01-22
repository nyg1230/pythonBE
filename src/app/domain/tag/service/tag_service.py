from app.domain.base.service.base_service import BaseService
from app.domain.tag.repository.tag_repository import TagRepository
from app.domain.tag.vo.tag_vo import TagVo

tag_repository = TagRepository()

class TagService(BaseService):
    def __init__(self):
        super().__init__()

    def create_tag(self, tag: TagVo):
        return tag_repository.create_tag(tag = tag)

    def create_tags(self, tags: list[TagVo]):
        return tag_repository.create_tags(tags = tags)

    def get_tags_by_target_oid(self, target_oid):
        result = tag_repository.get_tags_by_target_oid(target_oid)
        
        tags = []
        
        for data in result:
            tag = TagVo().create(**data)
            tags.append(tag)

        return tags