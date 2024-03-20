def main():
    print("Greeting: ", end="")
    Greeting = input().lower().strip()
    Output(Greeting)

def Output(Greeting):
    Greetings = Greeting.find("hello")
    if Greetings == 0:
        print("$0")
    elif Greeting[0] == "h":
        print("$20")
    else:
        print("$100")

main()