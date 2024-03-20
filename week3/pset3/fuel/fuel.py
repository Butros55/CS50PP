def main():
    print(f"{calc()}")


def calc():
    while True:
        fuel = input("Fraction: ")
        j = 1
        try:
            fuel_1 = ""
            fuel_2 = ""
            for i in fuel:
                if i == "/":
                    while j < len(fuel):
                        fuel_2 = fuel_2 + fuel[j]
                        j += 1
                    if j == len(fuel):
                        break
                fuel_1 = fuel_1 + i
                j += 1
            z = round(int(fuel_1) / int(fuel_2) * 100)
            if z > 100:
                pass
            elif z <= 1:
                return "E"
            elif z >= 99:
                return "F"
            else:
                return str(z) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()
