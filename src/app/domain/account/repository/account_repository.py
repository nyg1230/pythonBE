from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.account.vo.account_vo import AccountVo
from app.domain.user.vo.user_vo import UserVo
from app.common.param.where_vo import WhereVo

from operator import itemgetter

class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(AccountVo.entity)

    def insert_account(self, account_list: list):
        columns = ["oid", "user_oid", "target_date", "history", "amount", "memo", "category"]
        return self.multiple_insert(datas = account_list, columns = columns)
    
    def select_account(self, json: dict, user: UserVo) -> dict:
        where = WhereVo()
        where.set_where(f"user_oid = %s")
        where.set_param((user.get_oid(), ))
        accounts = super().select(AccountVo, json, where)

        return accounts