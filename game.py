import random

def typelevel():
    while True:
        level = input("Level: ")
        try:
            level=int(level)
        except ValueError:
            continue
        if level<=0:
            continue
        return level

def typeguess():
    while True:
        guess = input("Guess: ")
        try:
            guess=int(guess)
        except ValueError:
            continue
        if guess<=0:
            continue
        return guess

def main():
    level=typelevel()
    randomnumber = random.randint(1, level)
    while True:
        guess=typeguess()

        if guess < randomnumber:
            print("Too small!")
        elif guess > randomnumber :
            print("Too large!")
        else:
            print("Just right!")
            break

main()


