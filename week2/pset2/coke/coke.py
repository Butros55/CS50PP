def main():
    
    due = 50
    while due > 0:
        print("Amount Due:", due)
        coins = int(input("Insert Coin: "))

        if coins == 5:
            due = due - coins
        elif coins == 10:
            due = due - coins
        elif coins == 25:
            due = due - coins

        if due <= 0:
            print("Change Owed:", -due)


main()

