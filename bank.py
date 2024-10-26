def check():
    greeting = input("Greeting: ").lstrip().lower()
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        return "$20"
    else:
        return "$100"

def greet():
    result=check()
    print(result)

greet()

