# S3_LAM_06 — Map values in a dict

def map_values(d, fn):
    return {k: fn(v) for k, v in d.items()}


# tests
data = {"a": 1, "b": 2, "c": 3}

print(map_values(data, lambda x: x * 10))   # {'a': 10, 'b': 20, 'c': 30}
print(map_values(data, lambda x: x + 1))    # {'a': 2, 'b': 3, 'c': 4}
