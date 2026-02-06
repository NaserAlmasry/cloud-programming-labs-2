# S2_FOR_03 — Sum until threshold

def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total


# tests
print(sum_until([1, 2, 3, 4, 5], 7))    # 6 (1+2+3)
print(sum_until([5, 5, 5], 10))         # 10
print(sum_until([10, 1, 1], 9))          # 0
