# S3_LAM_02 — Sort by key using lambda

people = [
    {"name": "Ala", "age": 30},
    {"name": "Ola", "age": 22},
    {"name": "Jan", "age": 40},
]

print("before:", people)

sorted_people = sorted(people, key=lambda p: p["age"])

print("after:", sorted_people)
