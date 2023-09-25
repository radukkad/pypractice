import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    else:
        for argv in sys.argv[1:-1]:
            print(f" Hello, my name is {argv}")

main()