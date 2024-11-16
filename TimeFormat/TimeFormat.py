import re

def main():
    print(convert(input("Hours: ")))

def convert(hours):
    pattern = r"^(?P<first>1[0-2]|[1-9]):?(?P<second>[0-5]?\d)? (?P<firstpart>AM|PM) to (?P<third>1[0-2]|[1-9]):?(?P<fourth>[0-5]?\d)? (?P<secondpart>AM|PM)$"
    match = re.search(pattern, hours)
    if not match:
            raise ValueError

    first = int(match.group("first"))
    second = match.group("second")
    firstpart = match.group("firstpart")
    third = int(match.group("third"))
    fourth = match.group("fourth")
    secondpart = match.group("secondpart")
    if second is None:
        second = "00"
    if fourth is None:
        fourth = "00"
    second = int(second)
    fourth = int(fourth)

    if not (0 <= second < 60) or not (0 <= fourth < 60):
        raise ValueError

    if firstpart == "PM" and first != 12:
        first += 12
    elif firstpart == "AM" and first == 12:
        first = 0
    if secondpart == "PM" and third != 12:
        third += 12
    elif secondpart == "AM" and third == 12:
        third = 0

    start_time = f"{first:02}:{second:02}"
    end_time = f"{third:02}:{fourth:02}"
    return f"{start_time} to {end_time}"

if __name__ == "__main__":
    main()
