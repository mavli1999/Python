def main():
    expression=input("Expression: ")
    x, y, z = expression.split(" ")
    x=int(x)
    z=int(z)
    if y == "+":
        return result=x+z
    elif y == "-":
        return result=x-z
    elif y == "*":
        return result=x*z
    elif y == "/" and z != 0:
        return result=x/z
    else:
        return result="Error"

def check():
    final=main()
    print(final)

check()
