from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.account.vo.account_vo import AccountVo
from app.domain.user.vo.user_vo import UserVo
from app.common.param.where_vo import WhereVo
from app.common.util import common_util

from operator import itemgetter
from itertools import repeat

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
    
    def select_period_data(self, json: dict, user: UserVo):
        exclude = json.__getitem__("exclude")
        add_where = ""
        add_param = ()
        if (common_util.is_list(exclude)):
            add_where = f"""category not in ({", ".join(list(repeat("%s", exclude.__len__())))}) AND"""
            add_param = tuple(exclude)
        
        sql = f"""
        SELECT
            {", ".join(AccountVo.get_columns())}
        FROM
            {self.get_entity()}
        WHERE
            {add_where}
            target_date >= %s AND
            target_date <= %s AND
            user_oid = %s
        ORDER BY
            target_date ASC
        """
        
        param = (json.__getitem__("start_date"), json.__getitem__("end_date"), user.get_oid())
        param = add_param + param
        
        return ConnectionUtil.select(sql, param)
    
    def select_period_category_data(self, json: dict, user: UserVo):
        exclude = json.__getitem__("exclude")
        add_param = ()
        if (common_util.is_list(exclude)):
            add_where = f"""category not in ({", ".join(list(repeat("%s", exclude.__len__())))}) AND"""
            add_param = tuple(exclude)
        
        sql = f"""
        SELECT
            category, SUM(amount) as total
        FROM
            {self.get_entity()}
        WHERE
            {add_where}
            target_date >= %s AND
            target_date <= %s AND
            user_oid = %s
        GROUP BY
        GROUPING SETS
            ( (category) )
        ORDER BY
            total
        """
        
        param = (json.__getitem__("start_date"), json.__getitem__("end_date"), user.get_oid())
        param = add_param + param
        
        return ConnectionUtil.select(sql, param)