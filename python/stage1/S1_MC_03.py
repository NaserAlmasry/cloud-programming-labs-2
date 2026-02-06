def calc(a, op, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return None
            return a / b
        case _:
            return None


# tests
print(calc(10, "+", 5))   # 15
print(calc(10, "-", 5))   # 5
print(calc(10, "*", 5))   # 50
print(calc(10, "/", 5))   # 2.0
print(calc(10, "/", 0))   # None
print(calc(10, "x", 5))   # None
print(calc("10", "+", 5)) # None
