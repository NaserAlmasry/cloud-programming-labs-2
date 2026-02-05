# S1_IF_01 — Shipping cost

def shipping_cost(weight_kg, is_member):
    # validate weight
    try:
        w = float(weight_kg)
    except (TypeError, ValueError):
        return None

    if w <= 0:
        return None

    if w <= 1:
        cost = 10
    elif w <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8

    return cost

# tests (include boundaries)
tests = [
    (0, False),
    (-1, True),
    ("x", False),
    (0.5, False),
    (1, True),
    (1.01, False),
    (5, True),
    (5.01, False),
]

for w, m in tests:
    print(w, m, "->", shipping_cost(w, m))
