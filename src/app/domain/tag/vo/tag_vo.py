from app.domain.base.vo.base_vo import BaseVo

class TagVo(BaseVo):
    entity = "NMTag"
    columns = ["tag", "target_oid", "target_type"]
    __tag: str = None
    __target_type: str = None
    __target_oid: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def get_tag(self) -> str: return self.__tag
    def set_tag(self, tag): self.__tag = tag
    
    def get_target_type(self) -> str: return self.__target_type
    def set_target_type(self, t): self.__target_type = t
    
    def get_target_oid(self) -> str: return self.__target_oid
    def set_target_oid(self, oid): self.__target_oid = oid
