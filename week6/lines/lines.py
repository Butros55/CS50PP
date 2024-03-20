import sys


def main():

    #checking for Errors
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    #try to open File except isnt found
    try:
        print(get_lines(open(sys.argv[1])))
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_lines(file):

    lines = 0
    for line in file:
        if not (line.lstrip().startswith("#") or line.strip() == ''):
            lines += 1

    return lines



if __name__ == "__main__":
    main()