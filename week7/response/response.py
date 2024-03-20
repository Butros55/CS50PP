from validator_collection import checkers

def main():
    mail = input("Whats your email adress? ")
    if email := checkers.is_email(mail):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()