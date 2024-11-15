def value(greeting):
    greeting = greeting.lstrip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        return 20
    else:
        return 100

def main():
    greeting = input("Greeting: ")
    result=value(greeting)
    print(f"${result}")

if __name__ == "__main__":
    main()
