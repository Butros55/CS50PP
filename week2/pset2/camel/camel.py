def main():
    user = input("camelCase: ")
    camel(user)


def camel(user):
    n = 0
    print("snake_case: ", end="")
    for i in user:
        if user[n].isupper():
            print("_" + i.lower(), end="")
        else:
            print(i, end="")
        n = n + 1
    print("")

main()