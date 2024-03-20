import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if search := re.search(r"(?:<iframe){1}.*https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+).*(?:></iframe>){1}", s):
        return f"https://youtu.be/{search.group(1)}"


if __name__ == "__main__":
    main()