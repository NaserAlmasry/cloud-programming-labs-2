# S1_VAR_04 — Identity vs equality (is vs ==)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)   # same values
print("a is b:", a is b)   # different objects

print("a is c:", a is c)   # same object

x = None
print("x is None:", x is None)  # correct way to check None

# Use 'is' for identity (same object)
# Use '==' for equality (same value)
