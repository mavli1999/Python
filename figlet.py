from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()

    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")

    elif len(sys.argv) == 1:

        fonts=figlet.getFonts() #get the full list of fonts
        random_fonts=random.choices(fonts, k=1)[0] #returns a list with 1 item, then changes it into a string value
        figlet.setFont(font=random_fonts)

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f","--font"]:
            sys.exit("Invalid usage")

        elif sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")

        else:
            figlet.setFont(font=sys.argv[2])

    return figlet

def output(figlet):
    userinput = input("Input: ")
    print(figlet.renderText(userinput))

output(main())
W


