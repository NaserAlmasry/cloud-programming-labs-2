# S2_FOR_04 — Count occurrences

def count_occurrences(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts


# tests
print(count_occurrences([1, 2, 2, 3, 1, 1]))
print(count_occurrences(["a", "b", "a", "c", "b"]))
print(count_occurrences([]))
