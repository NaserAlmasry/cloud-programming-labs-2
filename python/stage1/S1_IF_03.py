# S1_IF_03 — Normalize user name

def normalize_name(x):
    if not x:
        return "Anonymous"

    name = str(x).strip()
    if name == "":
        return "Anonymous"

    return name


# tests
tests = ["", " ", None, " Ola "]

for t in tests:
    print(repr(t), "->", normalize_name(t))
