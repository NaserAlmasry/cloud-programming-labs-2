# S1_VAR_01 — Catalog of values and type()

values = {
    "int": 42,
    "float": 3.14,
    "str": "hello",
    "bool": True,
    "none": None,
    "list": [1, 2, 3],
    "tuple": (1, 2),
    "dict": {"a": 1},
    "set": {1, 2},
    "function": lambda x: x,
}

print(f"{'name':<10} {'value':<20} {'type(x)':<20} type_name")
print("-" * 70)

for name, v in values.items():
    print(f"{name:<10} {str(v):<20} {type(v):<20} {type(v).__name__}")
