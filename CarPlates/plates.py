def is_valid(s):
    # Check the length of the plate (2 to 6 characters)
    if not (2 <= len(s) <= 6):
        return False

    # Check that the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check that the plate contains only alphanumeric characters
    if not s.isalnum():
        return False

    # Check that numbers, if present, are only at the end and do not start with '0'
    found_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not found_digit:
                # First number must not be '0'
                if char == '0':
                    return False
            found_digit = True
        elif found_digit and char.isalpha():
            # If a letter appears after a number, it's invalid
            return False

    # If all checks pass, return True
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
