from app.domain.base.service.base_service import BaseService
from app.domain.tag.repository.tag_repository import TagRepository
from app.domain.tag.vo.tag_vo import TagVo

tag_repository = TagRepository()

class TagService(BaseService):
    def __init__(self):
        super().__init__()
