# S3_PIPE_04 — Iterable pipeline (generator-based)

def to_floats(values):
    for s in values:
        try:
            yield float(s.strip())
        except Exception:
            continue

def doubled(nums):
    for n in nums:
        yield n * 2

def pipeline_sum(values):
    return sum(doubled(to_floats(values)))


# tests
data = [" 1 ", "x", "2.5", "  -3 ", "", "10"]
print(pipeline_sum(data))  # (1 + 2.5 - 3 + 10) * 2 = 21.0
