def flatten1(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            for x in item:
                result.append(x)
        else:
            result.append(item)
    return result


# tests
print(flatten1([1, [2, 3], [4], 5]))      # [1, 2, 3, 4, 5]
print(flatten1([[1, 2], [3, 4]]))          # [1, 2, 3, 4]
print(flatten1([1, 2, 3]))                 # [1, 2, 3]
