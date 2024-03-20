def main():
    print("Expression: ")
    math = input()
    calculation(math)


def calculation(math):
    x, y, z = math.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        print(format(x + z, ".1f"))
    elif y == "-":
        print(format(x - z, ".1f"))
    elif y == "/":
        print(format(x / z, ".1f"))
    elif y == "*":
        print(format(x * z, ".1f"))

main()