# S3_DICT_06 — Group by property

def group_by(items, key):
    result = {}

    for item in items:
        if not isinstance(item, dict):
            continue
        value = item.get(key)

        if value in result:
            result[value].append(item)
        else:
            result[value] = [item]

    return result


# tests
people = [
    {"name": "Ala", "city": "Warsaw"},
    {"name": "Ola", "city": "Warsaw"},
    {"name": "Jan", "city": "Krakow"},
    {"name": "Mia", "city": "Gdansk"},
]

print(group_by(people, "city"))
