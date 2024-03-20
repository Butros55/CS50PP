def main():
    userinput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    userinput = userinput.strip().lower()
    (Answer(userinput))


def Answer(userinput):

    match userinput:
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "forty two":
            print("Yes")
        case _:
            print("No")

main()