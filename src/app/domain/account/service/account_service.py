from app.domain.base.service.base_service import BaseService
from app.domain.user.service.user_service import UserService
from app.domain.tag.service.tag_service import TagService
from app.domain.account.repository.account_repository import AccountRepository
from app.domain.account.vo.account_vo import AccountVo
from app.domain.tag.vo.tag_vo import TagVo
from app.common.param.page_vo import PageVo

from operator import itemgetter

account_repository = AccountRepository()

user_service = UserService()
tag_service = TagService()

class AccountService(BaseService):
    def __init__(self):
        super().__init__()

    def insert_account(self, account_list: list[dict]):
        new_list = []
        user = user_service.get_token_user()
        oid = user.get_oid()

        tags = []

        for d in account_list:
            account = AccountVo().create(**d)
            account.set_user_oid(oid)
            new_list.append(account)
            account_oid = account.get_oid()
            
            try:
                for t in d.__getitem__("tags"):
                    tag = TagVo().create(**t)
                    tag.set_target_oid(account_oid)
                    tag.set_target_type("account")
                    tags.append(tag)
            except Exception as e:
                print(e)
        
        
        result = account_repository.insert_account(new_list)
        
        if (tags.__len__() > 0): tag_service.create_tags(tags)

        return result
    
    def select_account(self, json):
        param, pageParam = itemgetter("param", "page")(json)
        page = PageVo(**pageParam)

        return account_repository.select_account(param, page)