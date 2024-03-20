def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if 2 <= len(s) <= 6:
        if s.isalpha():
            return True

        n = 0
        for i in s:
            if i.isdigit():
                if i == "0":
                    return False
                elif s[n:].isdigit():
                    return True
            else:
                n += 1


main()