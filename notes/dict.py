student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}


for key, value in student.items():
    print(key, value)

student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}

for value in student.values():
    value = None

print(student)

student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}

for key in student.keys():
    student[key] = None

print(student)

student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}

for key in student.keys():
    # if key.find("name") != -1:
        # student[key] = None
    if "name" in key:
        student[key] = None

print(student)

fruit = {
    "apples": 5,
    "pears": 2,
    "plums": 11,
    "peaches": 7
}

shopping_list = []

for fruit, qty in fruit.items():
    if qty <= 5:
        shopping_list.append(fruit)

print(shopping_list)
