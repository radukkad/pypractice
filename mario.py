def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width, end="")

def print_square(size):
    for i in range(size):
        print("#" * size)
def main():
    print_square(8)

main()