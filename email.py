#pip install validator-collection
from validator_collection import validators, checkers, errors

def check(email):
    is_email_address = checkers.is_email(email)
    if is_email_address is True:
        return "Valid"
    else:
        return "Invalid"

def main():
    print(check(input("What's your email address? ")))

main()