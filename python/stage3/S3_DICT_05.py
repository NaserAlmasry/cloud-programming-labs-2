# S3_DICT_05 — Invert dict with collisions

def invert(d):
    result = {}

    for k, v in d.items():
        if v in result:
            # collision → make it a list
            if isinstance(result[v], list):
                result[v].append(k)
            else:
                result[v] = [result[v], k]
        else:
            result[v] = k

    return result


# tests
print(invert({"a": 1, "b": 2}))              # {1: 'a', 2: 'b'}
print(invert({"a": 1, "b": 1, "c": 2}))      # {1: ['a', 'b'], 2: 'c'}
print(invert({"x": 5, "y": 5, "z": 5}))      # {5: ['x', 'y', 'z']}
