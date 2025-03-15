students = {
    "101": {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A",
        "courses": ["Math", "Physics", "Computer Science"],
        "attendance": 95
    },
    "102": {
        "name": "Bob Smith",
        "age": 21,
        "grade": "B",
        "courses": ["History", "Literature", "Political Science"],
        "attendance": 88
    },
    "103": {
        "name": "Charlie Brown",
        "age": 19,
        "grade": "A-",
        "courses": ["Biology", "Chemistry", "Physics"],
        "attendance": 92
    },
    "104": {
        "name": "Diana Adams",
        "age": 22,
        "grade": "C+",
        "courses": ["Economics", "Statistics", "Business"],
        "attendance": 80
    },
    "105": {
        "name": "Ethan Green",
        "age": 20,
        "grade": "B+",
        "courses": ["Computer Science", "Mathematics"],
        "attendance": 90
    }
}

# for key, value in students.items():
#     print(f'{key}:{value["name"]}')

# for key, value in students.items():
#     if "A" in value["grade"]:
#       print(f'{key}:{value["name"]}')

inp = input('input: ')
for key, value in students.items():
    if inp in value["courses"]:
        print(f'{key}:{value["name"]}')