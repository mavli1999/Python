def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit():
        raise ValueError
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    #intentionally raise errors to be caught later in a try-except
    return int(round((x / y) * 100))

def gauge(percentage):
    if 0<=percentage<=1:
        return "E"
    elif 99<=percentage<=100:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        fraction = input("Fraction: ")
        if "/" not in fraction:
            continue
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError): #catch the intentionally raised errors
             continue
        print(gauge(percentage))
        break

if __name__ == "__main__":
    main()
