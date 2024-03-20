def main():
    converted = convert(input("What time is it? "))
    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")

def convert(t):
    n = t.find(":") + 1
    h = ""
    m = ""

    for hours in t:
        if not hours.isdigit():
            break
        h = h + hours

    while n < len(t):
        if not t[n].isdigit():
            break
        m = m + t[n]
        n += 1

    if t[-4:] == "p.m.":
        m = float(m) / 60
        h = float(h) + 12

    else:
        m = float(m) / 60
        h = float(h)

    return h + m


if __name__ == "__main__":
    main()