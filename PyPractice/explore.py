name = input("Enter your name : ")
name = name.strip().title()
first, last = name.split(" ")
print(f"Hello, {name}")
print(last, first)