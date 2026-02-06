# S3_LAM_05 — Higher-order predicate

def at_least(min_value):
    return lambda x: x >= min_value


nums = [1, 5, 10, 15, 20]

filtered = list(filter(at_least(10), nums))
print(filtered)   # [10, 15, 20]
