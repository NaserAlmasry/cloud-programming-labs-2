# S1_VAR_09 — Type hints are not runtime enforcement

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))        # expected int
print(add("2", "3"))    # works, but not an int result

# Type hints help tools and readers,
# but Python does not enforce them at runtime.
