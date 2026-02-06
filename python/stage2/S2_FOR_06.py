# S2_FOR_06 — Sum nested lists (matrix)

def sum_nested(matrix):
    total = 0

    for row in matrix:
        if not isinstance(row, list):
            return None
        for x in row:
            total += x

    return total


# tests
print(sum_nested([[1, 2], [3, 4]]))     # 10
print(sum_nested([[5], [10, 20]]))      # 35
print(sum_nested([]))                   # 0
print(sum_nested([1, [2, 3]]))          # None
