import inflect

def getnames():
    names = []
    while True:
        try:
            name=input("Name: ")
            names.append(name)
        except EOFError:
            break
    return names

def main():
    names = getnames()
    p = inflect.engine()
    formatted_names = p.join(names)
    print(f"Adieu, adieu, to {formatted_names}")

main()

