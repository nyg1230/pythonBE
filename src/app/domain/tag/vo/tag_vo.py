from app.domain.base.vo.base_vo import BaseVo

class TagVo(BaseVo):
    entity = "NMTag"

    __json = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def to_json(self):
        return super().to_json(self.__json)