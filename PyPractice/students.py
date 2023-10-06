import csv

name = input("Enter name: ")
age = input("Enter age: ")
country = input("Enter country: ")
with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","age","country"])
    writer.writerow({"name": name, "age": age, "country":country});


students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is {student['age']} old and is from {student['country']}")