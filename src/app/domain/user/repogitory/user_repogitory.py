from app.domain.base.repogitory.base_repogitory import BaseRepogitory
from app.common.util.connection_util import ConnectionUtil
from app.domain.user.vo.user_vo import UserVo

global entity_name
entity_name = "NMUser"

class UserRepogitory(BaseRepogitory):
    def __init__(self):
        super().__init__(entity_name)
    
    def find_by_account(self, user: UserVo):
        account = user.get_account()
        sql = f"""
        SELECT
            *
        FROM
            {self.get_entity()}
        WHERE
            ACCOUNT = %s
        """
        result = ConnectionUtil.select_one(sql, (account, ))
        user = None if result is None else UserVo(**result)

        return user

    def signup(self, user: UserVo):
        sql = f"""
        INSERT INTO {self.get_entity()} (
            account,
            pwd,
            email,
            nickname,
            sex
        ) values ( %s, %s, %s, %s, %s )
        """
        
        param = (
            user.get_account(),
            user.get_pwd(),
            user.get_email(),
            user.get_nickname(),
            user.get_sex(),
        )
        
        return ConnectionUtil.execute(sql, param)