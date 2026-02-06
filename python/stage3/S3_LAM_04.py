# S3_LAM_04 — Sum of squares of even numbers

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
print("evens:", evens)

squares = list(map(lambda x: x * x, evens))
print("squares:", squares)

result = sum(squares)
print("result:", result)  # 56
