from app.domain.base.repogitory.base_repogitory import BaseRepogitory
from app.common.util.connection_util import ConnectionUtil
from app.domain.account.vo.account_vo import AccountVo

class AccountRepogitory(BaseRepogitory):
    def __init__(self):
        super().__init__(AccountVo.entity)

    def add_account_list(self, account_list: list):
        columns = ["oid", "user_oid", "target_date", "amount", "memo", "type"]
        result = self.multiple_insert(self.get_entity(), account_list, columns)

        print(result)
