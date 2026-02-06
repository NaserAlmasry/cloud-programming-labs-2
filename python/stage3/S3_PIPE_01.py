# S3_PIPE_01 — pipe(*fns)

def pipe(*fns):
    def runner(x):
        value = x
        for fn in fns:
            value = fn(value)
        return value
    return runner


# tests
add1 = lambda x: x + 1
times2 = lambda x: x * 2
minus3 = lambda x: x - 3

p = pipe(add1, times2, minus3)

print(p(10))  # ((10+1)*2)-3 = 19
print(p(0))   # ((0+1)*2)-3 = -1
