from app.domain.base.vo.base_vo import BaseVo

class UserVo(BaseVo):
    __table = "NMUser"
    __account = ""
    __pw = ""

    def __init__(self):
        super().__init__(UserVo)