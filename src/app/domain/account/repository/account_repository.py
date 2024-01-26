from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.account.vo.account_vo import AccountVo
from app.common.param.where_vo import WhereVo

from operator import itemgetter

class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(AccountVo.entity)

    def insert_account(self, account_list: list):
        columns = ["oid", "user_oid", "target_date", "history", "amount", "memo", "type", "category"]
        return self.multiple_insert(datas = account_list, columns = columns)
    
    def select_account(self, json: dict) -> dict:
        where = WhereVo()
        where.set_where()
        accounts = super().select(AccountVo, json, where)

        return accounts