def group_dict_list_by(data_list, group_by_key):
    result = {}
    for x in data_list:
        key = x.get(group_by_key)
        if key:
            if key not in result:
                result[key] = []
            result[key].append(x)
    return result
