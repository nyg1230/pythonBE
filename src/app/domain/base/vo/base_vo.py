import json
import uuid

class BaseVo():
    entity = None
    columns = []
    __oid = None
    __created_date = None
    __modified_date = None
    
    columns = ["oid", "created_date", "modified_date"]

    def __init__(self, *args, **kwargs):
        self.set(kwargs)
    
    def create(self, **kwargs):
        self.set(kwargs)
        self.set_oid(uuid.uuid1().hex)
        return self
    
    def get_entity(self):
        return self.__class__.entity

    def get_oid(self): return self.__oid
    def set_oid(self, oid): self.__oid = oid
    
    def get_created_date(self): return self.__created_date
    def set_created_date(self, date): self.__created_date = date
    
    def get_modified_date(self): return self.__modified_date
    def set_modified_date(self, date): self.__modified_date = date
    
    def get_value(self, key: str):
        value = None
        try:
            value = self.__getattribute__(f"get_{key}")()
        except:
            value = None

        return value
    
    @classmethod
    def get_columns(cls):
        return [*BaseVo.columns, *cls.columns]
    
    @classmethod
    def has_columns(cls, vo = None, has_oid = True):
        columns = cls.get_columns()
        contains = []
        for col in columns:
            try:
                if (has_oid or col is not "oid"):
                    v = vo.get_value(col)
                    if (v is not None): contains.append(col)
            except:
                continue

        return contains

    def set(self, obj: dict):
        for key in obj:
            try:
                self.__getattribute__(f"set_{key}")(obj[key])
            except:
                continue

    def to_dict(self):
        d = dict()

        keys = [*self.columns, *self.get_columns()]

        for key in keys:
            try:
                d.__setitem__(key, self.__getattribute__(f"get_{key}")())
            except:
                continue

        return d

    def to_json(self):
        return json.dumps(self.to_dict(), default=str, ensure_ascii=False)