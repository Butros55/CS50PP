def main():
    user = input("Input: ")
    print(shorten(user))


def shorten(user):

    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    print("Output: ", end="")
    test = ""
    for i in user:
        found = False
        for j in vowels:
            if j == i:
                found = True
                break
        if found == False:
            test = test + i

    return test

if __name__ == "__main__":
    main()