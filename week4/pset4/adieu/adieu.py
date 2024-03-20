import inflect
p = inflect.engine()


def main():
    print(f"Adieu, adieu, to {get_input()}")


def get_input():
    names = []
    while True:
        try:
            name = input("Name: ").strip().title()
            names.append(name)
        except EOFError:
            return p.join(names)

main()