from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain._sample.vo.user_vo import SampleVo

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(SampleVo.entity)