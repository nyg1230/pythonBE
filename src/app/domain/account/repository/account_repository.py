from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.account.vo.account_vo import AccountVo

class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(AccountVo.entity)

    def add_account_list(self, account_list: list):
        columns = ["oid", "user_oid", "target_date", "amount", "memo", "type"]
        result = self.multiple_insert(self.get_entity(), account_list, columns)

        print(result)
