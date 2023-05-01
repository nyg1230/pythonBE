from app.domain.base.service.base_service import BaseService
from app.domain.user.repogitory.user_repogitory import UserRepogitory

class UserService(BaseService):
    def __init__(self):
        super().__init__(UserRepogitory)
    