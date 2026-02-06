def unique(values):
    result = []
    for v in values:
        if v not in result:
            result.append(v)
    return result


# tests
print(unique([1, 2, 2, 3, 1]))          # [1, 2, 3]
print(unique(["a", "b", "a", "c"]))     # ['a', 'b', 'c']
print(unique([]))                       # []
