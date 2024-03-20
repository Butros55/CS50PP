def main():
    print("$" + str(value(input("Greeting: "))))

def value(greet):
    greetings = greet.lower().strip()
    if greetings.find("hello") == 0:
        return 0
    elif greetings[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()