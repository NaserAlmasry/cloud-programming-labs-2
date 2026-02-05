# S1_VAR_06 — Safe conversion: int() / float()

def to_int_or_none(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None

tests = ["12", " 12 ", "12x", "", None]

for t in tests:
    print(f"input={t!r:>6} -> output={to_int_or_none(t)}")
