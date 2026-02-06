# S3_PIPE_02 — compose(*fns)

def compose(*fns):
    def runner(x):
        value = x
        for fn in reversed(fns):
            value = fn(value)
        return value
    return runner


# compare with pipe idea using same functions
add1 = lambda x: x + 1
times2 = lambda x: x * 2
minus3 = lambda x: x - 3

c = compose(add1, times2, minus3)  # add1(times2(minus3(x)))

print(c(10))  # add1(times2(7)) = 15
print(c(0))   # add1(times2(-3)) = -5
