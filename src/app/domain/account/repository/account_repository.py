from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.account.vo.account_vo import AccountVo
from app.common.param.page_vo import PageVo

from operator import itemgetter

class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(AccountVo.entity)

    def insert_account(self, account_list: list):
        columns = ["oid", "user_oid", "target_date", "history", "amount", "memo", "type", "category"]
        return self.multiple_insert(datas = account_list, columns = columns)
    
    def select_account(self, param: dict = None, page: PageVo = PageVo()) -> list[AccountVo]:
        to_date = param.get("to_date")
        from_date = param.get("from_date")

        sql = f"""
        SELECT
            {", ".join(AccountVo.columns)}
        FROM
            {self.get_entity()}
        {page.get_query()}
        """

        result = ConnectionUtil.execute(sql, ())
        accounts = []
        for d in result:
            account = AccountVo(**d)
            accounts.append(account)
            
        return accounts