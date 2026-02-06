def clean_numbers(values):
    result = []
    for s in values:
        try:
            num = float(s.strip())
            result.append(num)
        except Exception:
            # drop invalid items
            pass
    return result


# tests
print(clean_numbers([" 1 ", "x", "2"]))          # [1.0, 2.0]
print(clean_numbers([" 3.5 ", "  -2 ", ""]))     # [3.5, -2.0]
print(clean_numbers(["10", " 10.0 ", "abc"]))    # [10.0, 10.0]
