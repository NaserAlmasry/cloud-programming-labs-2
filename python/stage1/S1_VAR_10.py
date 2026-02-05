# S1_VAR_10 — Mini inspector

def inspect(v):
    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": _is_iterable(v),
        "truthy": bool(v),
    }

def _is_iterable(v):
    try:
        iter(v)
        return True
    except TypeError:
        return False


values = [
    0,
    1,
    "",
    "hi",
    [],
    [1, 2],
    {},
    None,
    lambda x: x,
    (1, 2),
]

for v in values:
    print(v, "->", inspect(v))
