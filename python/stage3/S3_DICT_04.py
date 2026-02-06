# S3_DICT_04 — Omit keys

def omit(d, keys):
    result = {}
    for k, v in d.items():
        if k not in keys:
            result[k] = v
    return result


# tests
data = {"a": 1, "b": 2, "c": 3}

print(omit(data, ["a"]))        # {'b': 2, 'c': 3}
print(omit(data, ["b", "c"]))   # {'a': 1}
print(omit(data, []))           # {'a': 1, 'b': 2, 'c': 3}
