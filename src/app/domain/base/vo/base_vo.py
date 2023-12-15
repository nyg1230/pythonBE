import json
import uuid

class BaseVo():
    __entity = None
    __oid = None

    def __init__(self, entity, *args, **kwargs):
        self.__entity = entity
        self.set(kwargs)
    
    def create(self, **kwargs):
        self.set(kwargs)
        self.set_oid(uuid.uuid1().bytes)
        return self
    
    def get_entity(self):
        return self.__entity

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

    def to_json(self, keys = []):
        d = dict()

        for key in keys:
            try:
                d.__setitem__(key, self.__getattribute__(f"get_{key}")())
            except:
                continue

        return json.dumps(d, default=str)