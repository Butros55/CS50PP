def main():
    calc(get_input())


def get_input():
    s_list = {}
    while True:
        try:
            user = input().upper()
            s_list[user] = s_list[user] + 1
        except EOFError:
            return s_list
        except KeyError:
            s_list[user] = 1


def calc(list):
    for key, value in sorted(list.items()):
        print(f"{value} {key}")


main()
