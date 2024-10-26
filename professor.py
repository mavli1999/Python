import random

def get_level():
    while True:
        level=input("Level: ")
        try:
            level=int(level)
        except ValueError:
            continue

        if level not in [1,2,3]:
            continue
        else:
            return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x,y

def main():
    score=0
    n = get_level()
    for _ in range(0,10):
        x,y = generate_integer(n)
        problem = x + y
        answer=int(input(f"{x} + {y} = "))
        if answer == problem:
            score+=1

        elif answer != problem:
            print("EEE")
            for _ in range(0,2):
                if answer == problem:
                    break
                else:
                    answer=int(input(f"{x} + {y} = "))
                    print("EEE")
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
