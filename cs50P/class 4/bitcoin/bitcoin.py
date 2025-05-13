import requests
import sys
import json

def main():
    try:
        if len(sys.argv) == 2:
            number = float(sys.argv[1])
        else:
            raise ValueError
    except ValueError:
        sys.exit("wrong number specified")
    try:
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = bitcoin.json()
        result = number * float(o["bpi"]["USD"]["rate_float"])
        print(f"${result:,.04f}")
    except requests.RequestException:
        sys.exit("error")

main()



