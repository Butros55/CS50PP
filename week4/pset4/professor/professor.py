import random


def main():
    maths = generate_integer(get_level())
    points = 0
    for i in maths:
        x = i['x']
        y = i['y']
        for j in range(3):
            try:
                calc = int(input(f"{x} + {y} = "))
                if calc == x + y:
                    points += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                if j >= 2:
                    print(f"{x} + {y} = {x + y}")

    print(f"Score: {points}")


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl == 1 or lvl == 2 or lvl == 3:
                return int(lvl)
        except ValueError:
            pass


def generate_integer(level):
    maths = []
    if level == 1:
        lvl_x = 0
        lvl_y = 9
    elif level == 2:
        lvl_x = 10
        lvl_y = 99
    else:
        lvl_x = 100
        lvl_y = 999

    for _ in range(10):
        x = random.randint(lvl_x, lvl_y)
        y = random.randint(lvl_x, lvl_y)
        maths.append({"x":x, "y":y})
    return maths


if __name__ == "__main__":
    main()