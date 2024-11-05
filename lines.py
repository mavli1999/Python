import sys

def user_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.py'):
        sys.exit("Not a Python file")
    else:
        filename = sys.argv[1]
        return filename

def main():
    code_lines = 0
    filename = user_input()
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                elif line.strip().startswith("#"):
                    continue
                else:
                    code_lines +=1
            print(code_lines)
    except FileNotFoundError:
        sys.exit("File does not exist")

main()


