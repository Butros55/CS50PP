import sys
from tabulate import tabulate

def main():
    #check errors
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    print(tabulate(get_table(sys.argv[1]), headers="firstrow", tablefmt="grid"))


def get_table(file):
    try:
        menu = []
        with open(file) as file:
            for line in file:
                pizza, small, large = line.rstrip().split(",")
                menus = {"pizza": pizza, "small": small, "large": large}
                menu.append(menus)
            return menu

    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()