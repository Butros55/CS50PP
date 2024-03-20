import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if search := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if (
            0 <= int(search.group(1)) <= 255
            and 0 <= int(search.group(2)) <= 255
            and 0 <= int(search.group(3)) <= 255
            and 0 <= int(search.group(4)) <= 255
        ):
            return True

    return False


if __name__ == "__main__":
    main()
