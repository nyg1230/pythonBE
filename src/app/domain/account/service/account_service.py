from app.domain.base.service.base_service import BaseService
from app.domain.account.repository.account_repogitory import AccountRepogitory
from app.domain.account.vo.account_vo import AccountVo

account_repository = AccountRepogitory()

class AccountService(BaseService):
    def __init__(self):
        super().__init__()

    def add_account_list(self, account_list: list):
        new_list = []
        for d in account_list:
            account = AccountVo().create(**d)
            new_list.append(account)
        return account_repository.add_account_list(new_list)