# S1_VAR_03 — Mutability: list vs tuple

lst = [1, 2, 3]
lst[0] = 99
print("list:", lst)

tup = (1, 2, 3)
try:
    tup[0] = 99
except TypeError as e:
    print("tuple error:", e)

# Lists are mutable (you can change elements).
# Tuples are immutable (you cannot change elements after creation).
