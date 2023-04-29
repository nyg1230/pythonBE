def is_string(obj):
    return isinstance(obj, str)

def is_list(obj):
    return isinstance(obj, list)

def is_tuple(obj):
    return isinstance(obj, tuple)

def is_dict(obj):
    return isinstance(obj, dict)

def merge(target = dict, obj = dict):
    for k, v in target.items():
        if is_dict(v):
            node = obj.setdefault(k, {})
            merge(node, v)
        else:
            obj[k] = v
    return obj

def find(obj, key, default_value = None, split_str = "."):
    path = ""
    if (is_list(key)): path = key
    elif (is_string(key)): path = str(key).split(split_str)
    else: return default_value
    
    result = obj
    try:
        for p in path:
            if (is_dict(result)):
                result = dict(result).get(p)
            elif (is_list):
                result = list(result).__getitem__(int(p))
            elif (is_tuple(result)):
                result = tuple(result).__getitem__(int(p))
            else:
                result = default_value
                break
    except:
        result = default_value
    
    return result
