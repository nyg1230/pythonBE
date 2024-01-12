from app.domain.base.service.base_service import BaseService
from app.domain.user.service.user_service import UserService
from app.domain.account.repository.account_repository import AccountRepository
from app.domain.account.vo.account_vo import AccountVo

account_repository = AccountRepository()

user_service = UserService()

class AccountService(BaseService):
    def __init__(self):
        super().__init__()

    def add_account_list(self, account_list: list):
        new_list = []
        user = user_service.get_token_user()
        oid = user.get_oid()

        for d in account_list:
            account = AccountVo().create(**d)
            account.set_user_oid(oid)
            new_list.append(account)
        return account_repository.add_account_list(new_list)