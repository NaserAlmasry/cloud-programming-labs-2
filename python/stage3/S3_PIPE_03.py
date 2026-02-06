# S3_PIPE_03 — String normalization pipeline

import re

def pipe(*fns):
    def runner(x):
        value = x
        for fn in fns:
            value = fn(value)
        return value
    return runner


strip_ = lambda s: s.strip()
lower_ = lambda s: s.lower()
collapse_spaces = lambda s: re.sub(r"\s+", " ", s)

normalize = pipe(strip_, lower_, collapse_spaces)

print(normalize(" Ala   Ma   Kota "))  # "ala ma kota"
print(normalize("  HELLO    WORLD  "))  # "hello world"
