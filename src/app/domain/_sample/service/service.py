from app.domain.base.service.base_service import BaseService
from app.domain._sample.repository.sample_repository import SampleRepository
from app.domain._sample.vo.vo import Vo

sample_repository = SampleRepository()

class UserService(BaseService):
    def __init__(self):
        super().__init__()
