import re

def main():
    print(count(input("Text: ")))


def count(userinput):
    pattern = r"\bum\b"
    matches = re.findall(pattern, userinput, re.IGNORECASE) #return a list of what it found
    number = len(matches)
    return number

if __name__ == "__main__":
    main()