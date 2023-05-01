from app.domain.base.repogitory.base_repogitory import BaseRepogitory

global entity_name
entity_name = "uusseerr"

class UserRepogitory(BaseRepogitory):
    def __init__(self):
        super().__init__(entity_name)