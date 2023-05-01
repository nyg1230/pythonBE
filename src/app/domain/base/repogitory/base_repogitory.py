class BaseRepogitory():
    def __init__(self, entity):
        self.__entity = entity
    
    def get_entity(self):
        return self.__entity
        
    def find_by_oid(self, oid):
        print(f"repo find_by_oid {self.__entity} {oid}")