from app.domain.base.repository.base_repository import BaseRepository
from app.common.util.connection_util import ConnectionUtil
from app.domain.user.vo.user_vo import UserVo

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserVo.entity)
    
    def find_by_account(self, user: UserVo):
        account = user.get_account()
        sql = f"""
        SELECT
            oid, account, pwd, email, nickname, sex
        FROM
            {user.get_entity()}
        WHERE
            ACCOUNT = %s
        """
        result = ConnectionUtil.select_one(sql, (account, ))
        user = None if result is None else UserVo(**result)

        return user

    def signup(self, user: UserVo):
        sql = f"""
        INSERT INTO {user.get_entity()} (
            oid, account, pwd, email, nickname, sex
        ) values (
            %s, %s, %s, %s, %s, %s
        )
        returning {user.get_entity()}
        """
        
        param = (
            user.get_oid(),
            user.get_account(),
            user.get_pwd(),
            user.get_email(),
            user.get_nickname(),
            user.get_sex(),
        )
        
        return ConnectionUtil.execute(sql, param)