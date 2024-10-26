def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x=int(x)
            y=int(y)
            if x>y:
                continue

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

        else:
            return x/y

def get_fuel_status(division):
        if 0<=division<=0.01:
            print("E")
        elif 0.99<=division<=1:
            print("F")
        else:
            percentage = f"{round(division * 100)}%"
            print(percentage)

def main():
    get_fuel_status(get_fraction())

main()
