def active_user_names(users):
    return sorted(
        [u["name"].upper() for u in users if u.get("active") is True]
    )


# tests
users = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "bob", "active": False},
    {"id": 3, "name": "Charlie", "active": True},
    {"id": 4, "name": "dave", "active": True},
]

print(active_user_names(users))
# ['ALICE', 'CHARLIE', 'DAVE']
