class BaseVo():
    __oid = None

    def __init__(self, *args, **kwargs):
        self.__oid = None
        self.set(kwargs)

    def get_oid(self):
        return self.__oid

    def set_oid(self, oid):
        self.__oid = oid
        
    def set(self, obj: dict):
        for key in obj:
            try:
                self.__getattribute__(f"set_{key}")(obj[key])
            except:
                continue