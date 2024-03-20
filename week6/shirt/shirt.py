import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png")):
        sys.exit("Invalid output")
    elif not (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png")):
        sys.exit("Invalid input")
    elif sys.argv[1][-3:] != sys.argv[2][-3:]:
        sys.exit("Input and output have different extensions")

    change_picture()


def change_picture():
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as input:
        new = ImageOps.fit(input, shirt.size)
        new.paste(shirt, mask = shirt)
        new.save(sys.argv[2])


if __name__ == "__main__":
    main()