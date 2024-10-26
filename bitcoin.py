import sys
import requests

def backend():
    if len(sys.argv) == 0 or len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        try:
            sys.argv[1] = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    return sys.argv[1]

def main():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price = r.json()["bpi"]["USD"]["rate_float"] #get the value of a key that's a value of another key... within a dic

    #r.json() parses that JSON content and returns it as a dictionary/list

    sys.argv[1] = backend()
    amount = sys.argv[1] * price

    print(f"${amount:,.4f}")

main()

