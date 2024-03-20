import requests
import sys
import json

def main():

    try:
        if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")
        arg = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    print((f"${get_value():,.4f}"))

def get_value():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        return float(r.json()["bpi"]["USD"]["rate_float"]) * float(sys.argv[1])

    except requests.RequestException:
        sys.exit()


main()