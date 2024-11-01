def userinput(type):
    snake_case=""

    for camelcase in type:
        if camelcase.isupper():
            snake_case += "_" + camelcase.lower()
        else:
            snake_case += camelcase
    return snake_case

def main():
    type=input("camelCase: ")
    print("snake_case:", userinput(type))

main()
