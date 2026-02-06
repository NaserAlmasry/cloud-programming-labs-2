# S3_LAM_01 — Convert to lambdas

square = lambda n: n * n
is_odd = lambda n: n % 2 == 1
greet = lambda name: f"Hello, {name}!"

# tests (3 each)
print(square(2), square(0), square(-3))          # 4 0 9
print(is_odd(1), is_odd(2), is_odd(99))          # True False True
print(greet("Ala"), greet("Ola"), greet("Jan"))  # Hello, ...
