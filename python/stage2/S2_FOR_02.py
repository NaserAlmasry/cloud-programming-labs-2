# S2_FOR_02 — Find first even

def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None


# tests
print(find_first_even([1, 3, 5, 8, 10]))   # 8
print(find_first_even([1, 3, 5]))          # None
print(find_first_even([]))                 # None
