# S1_VAR_02 — Rebinding and dynamic typing

x = 10
print(x, type(x).__name__)

x = 3.14
print(x, type(x).__name__)

x = "hello"
print(x, type(x).__name__)

x = True
print(x, type(x).__name__)

# Dynamic typing means the same variable name can be
# rebound to values of different types at runtime.
