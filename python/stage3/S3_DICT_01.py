# S3_DICT_01 — Safe get by dotted path

def get_path(obj, path, fallback=None):
    parts = path.split(".")
    current = obj

    for p in parts:
        if not isinstance(current, dict):
            return fallback
        if p not in current:
            return fallback
        current = current[p]

    return current


# tests
data = {
    "a": {
        "b": {
            "c": 42
        }
    }
}

print(get_path(data, "a.b.c", "X"))     # 42
print(get_path(data, "a.b", "X"))        # {'c': 42}
print(get_path(data, "a.b.c.d", "X"))    # X
print(get_path(data, "a.x.c", "X"))      # X
print(get_path(data, "a.b.c", None))     # 42
