# S3_LAM_03 — Closure factory

def make_adder(x):
    return lambda y: x + y


# tests
add10 = make_adder(10)
add3 = make_adder(3)

print(add10(5))   # 15
print(add10(0))   # 10
print(add3(7))    # 10
