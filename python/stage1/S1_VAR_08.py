# S1_VAR_08 — Big integers

big_int = 10 ** 100
print("big_int:", big_int)
print("type:", type(big_int).__name__)
print("digits:", len(str(big_int)))

big_float = float(10 ** 100)
print("big_float:", big_float)

# Python integers have arbitrary precision.
# Floats lose precision for very large numbers.
