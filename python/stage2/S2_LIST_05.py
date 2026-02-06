def stats(nums):
    if not nums:
        return None

    total = sum(nums)
    return {
        "min": min(nums),
        "max": max(nums),
        "avg": total / len(nums),
        "sum": total,
    }


# tests
print(stats([1, 2, 3, 4]))        # min=1, max=4, avg=2.5, sum=10
print(stats([-5, 0, 5]))          # min=-5, max=5, avg=0
print(stats([]))                  # None
