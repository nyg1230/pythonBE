from app.domain.base.repogitory.base_repogitory import BaseRepogitory
from app.domain.user.vo.user_vo import UserVo

global entity_name
entity_name = "uusseerr"

class UserRepogitory(BaseRepogitory):
    def __init__(self):
        super().__init__(entity_name)
    
    def find_by_account(self, user: UserVo):
        return UserVo()