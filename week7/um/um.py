import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    print(re.search(r"um", s))


if __name__ == "__main__":
    main()