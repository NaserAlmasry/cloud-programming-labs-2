# S1_VAR_05 — Truthiness

def is_truthy(v):
    return bool(v)

tests = [0, 1, "", "0", [], [0], {}, None]

for t in tests:
    print(f"value={t!r:>6} -> truthy={is_truthy(t)}")
