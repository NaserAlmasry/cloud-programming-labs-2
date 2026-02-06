def day_name(n: int):
    match n:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case 7: return "Sunday"
        case _: return None


# tests
print(day_name(1))
print(day_name(7))
print(day_name(9))
