from operator import itemgetter
from app.common.util import jwt_util
from app.domain.base.service.base_service import BaseService
from app.domain.user.repogitory.user_repogitory import UserRepogitory
from app.domain.user.vo.user_vo import UserVo

user_repogitory = UserRepogitory()

class UserService(BaseService):
    def __init__(self):
        super().__init__()

    def get_token_user(self):
        user = jwt_util.get_current_user()
        account = itemgetter("account")(user)
        return self.find_by_account(UserVo(account = account))

    def find_by_account(self, user: UserVo):
        return user_repogitory.find_by_account(user)
    
    def signup(self, user: UserVo):
        return user_repogitory.signup(user)