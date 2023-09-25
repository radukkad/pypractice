def main():
    x = get_input("What's x? ")
    print(f"x is {x}")
def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()