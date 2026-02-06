# S3_PIPE_06 — Safe pipeline

def pipe_safe(*fns):
    def runner(x):
        value = x
        try:
            for fn in fns:
                value = fn(value)
            return {"ok": True, "value": value}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return runner


# example functions
def div10(x):
    return 10 / x

def add5(x):
    return x + 5


safe_pipeline = pipe_safe(div10, add5)

print(safe_pipeline(2))   # ok
print(safe_pipeline(0))   # division by zero → error
