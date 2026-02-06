# S3_DICT_03 — Pick keys

def pick(d, keys):
    result = {}
    for k in keys:
        if k in d:
            result[k] = d[k]
    return result


# tests
data = {"a": 1, "b": 2, "c": 3}

print(pick(data, ["a", "c"]))        # {'a': 1, 'c': 3}
print(pick(data, ["b", "x"]))        # {'b': 2}
print(pick(data, []))                # {}
