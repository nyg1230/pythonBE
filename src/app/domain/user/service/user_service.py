from app.domain.base.service.base_service import BaseService
from app.domain.user.repogitory.user_repogitory import UserRepogitory
from app.domain.user.vo.user_vo import UserVo

user_repogitory = UserRepogitory()

class UserService(BaseService):
    def __init__(self):
        super().__init__()
    
    def find_by_account(self, user: UserVo):
        return user_repogitory.find_by_account(user)