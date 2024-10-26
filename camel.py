type=input("camelCase: ")

snake_case=""

for camelcase in type:
    if camelcase.isupper():
        snake_case += "_" + camelcase.lower()
    else:
        snake_case += camelcase

print("snake_case:", snake_case)
