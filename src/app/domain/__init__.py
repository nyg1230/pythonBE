from enum import Enum

class method_enum(Enum):
    GET     = "C"
    POST    = "R"
    PUT     = "U"
    DELETE  = "D"
    
    def get(methods):
        method_list = []
        for m in methods:
            if (m in method_enum._value2member_map_):
                method_list.append(method_enum(m).name)
        return method_list
