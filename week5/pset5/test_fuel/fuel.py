def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) / int(y) > 1:
        raise ValueError
    return round(float(x) / float(y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
