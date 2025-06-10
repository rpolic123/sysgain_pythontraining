
students = [
    {"id": 1, "name": "John", "marks": {"math": 80, "science": 75}},
    {"id": 2, "name": "Jane", "marks": {"math": 90, "science": 85}}
]

for student in students:
    print(student["name"])
    print("--------------------")
    for subjct,marks in student['marks'].items():
        print(subjct,marks)