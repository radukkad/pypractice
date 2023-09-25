with open("names.txt") as file:
    for line in sorted(file):
        print(line.rstrip('\n'))