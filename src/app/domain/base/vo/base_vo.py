import json
import uuid

class BaseVo():
    entity = None
    __oid = None
    __created_date = None
    __modified_date = None
    
    __json = ["oid", "created_date", "modified_date"]

    def __init__(self, *args, **kwargs):
        self.set(kwargs)
    
    def create(self, **kwargs):
        self.set(kwargs)
        self.set_oid(uuid.uuid1().hex)
        return self
    
    def get_entity(self):
        print(self)
        return self.__class__.entity

    def get_oid(self): return self.__oid
    def set_oid(self, oid): self.__oid = oid
    
    def get_created_date(self): return self.__created_date
    def set_created_date(self, date): self.__created_date = date
    
    def get_modified_date(self): return self.__modified_date
    def set_modified_date(self, date): self.__modified_date = date

    def set(self, obj: dict):
        for key in obj:
            try:
                self.__getattribute__(f"set_{key}")(obj[key])
            except:
                continue

    def to_json(self, keys = []):
        d = dict()

        keys = [*self.__json, *keys]

        for key in keys:
            try:
                d.__setitem__(key, self.__getattribute__(f"get_{key}")())
            except:
                continue

        return json.dumps(d, default=str)