def main():
    print(seperate())



def seperate():
    while True:
        try:
            promt = input("Date: ")
            if promt.find("/") != -1:
                m, d, y = promt.split("/")
            elif promt.find(" ") != -1 and promt.find(",") != -1:
                m, d, y = promt.split(" ")
                m  = list.index(m) + 1
                d = d.strip(",")

            return get_date(int(m), int(d), int(y))

        except (UnboundLocalError, ValueError):
            pass

def get_date(m, d, y):
    if m <= 12 and d <= 31:
        date = f"{y}-{m:02}-{d:02}"
        return date
    else:
        seperate()














list = ["January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

main()