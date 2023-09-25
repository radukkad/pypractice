students  = [
    {"name": "Rajesh", "place" : "USA", "age" : 45},
    {"name": "Girish", "place": "kerala", "age": 43},
    {"name": "Ratheesh", "place": "bangalore", "age": 41}
]

for student in students:
    print(student["name"], student["place"], student["age"], sep=",")
    #print(student, students[student], sep=",")