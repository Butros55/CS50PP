from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()


def main():
    # checking for errors
    try:
        if len(sys.argv) == 1:
            pass
        elif "-f" != sys.argv[1] != "--font" or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        transform()
    except IndexError:
        sys.exit("Invalid usage")


def transform():
    if len(sys.argv) == 1:
        figlet.setFont(font=fonts[random.randint(0, len(fonts))])
    else:
        figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input("Input: ")))


main()
