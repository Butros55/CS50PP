import random
import sys

def main():
    play_state(set_level())


def set_level():
    while True:
        try:
            ran = random.randint(1, int(input("Level: ")))
            return ran
        except ValueError:
            pass

def play_state(ran):
    while True:
        try:
            n = int(input("Guess: "))
            if n < ran:
                print("Too small!")
            elif n > ran:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            pass

main()