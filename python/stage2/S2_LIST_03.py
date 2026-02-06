def chunk(lst, size):
    if size <= 0:
        return None

    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i + size])
    return result


# tests
print(chunk([1, 2, 3, 4, 5], 2))   # [[1, 2], [3, 4], [5]]
print(chunk([1, 2, 3], 3))         # [[1, 2, 3]]
print(chunk([1, 2, 3], 0))         # None
