from datetime import datetime

def to_dict(obj):
    if hasattr(obj, 'attribute_map'):
        result = {}
        for k,v in getattr(obj, 'attribute_map').items():
            val = getattr(obj, k)
            if val is not None:
                result[v] = to_dict(val)
        return result
    elif type(obj) == list:
        return [to_dict(x) for x in obj]
    elif type(obj) == datetime:
        return str(obj)
    else:
        return obj

def truncate_list_of_dicts_by_key(list_of_dicts, key):
    result = []
    for item in list_of_dicts:
        result.append(deep_dict_value(item,key))
    return result

def deep_dict_value(data, key):
    print("----- deep_dict_value ------")
    layers = key.split('.')
    print(layers)
    for layer in layers:
        print(data)
        data = data[layer]
   
    return data