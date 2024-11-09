import sys
from PIL import Image, ImageOps
import os

def userinput():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >3:
        sys.exit("Too many command-line arguments")

    else:
        root1, ext1 = os.path.splitext(sys.argv[1])
        root2, ext2 = os.path.splitext(sys.argv[2])
        if ext1.strip().lower() not in (".jpg", ".jpeg", ".png") or ext2.strip().lower() not in (".jpg", ".jpeg", ".png"):
            sys.exit("Invalid output")
        elif ext1.strip().lower() != ext2.strip().lower():
            sys.exit("Input and output have different extensions")
        else:
            beforeimg = sys.argv[1]
            afterimg = sys.argv[2]
    return beforeimg, afterimg

def main():
    beforeimg, afterimg = userinput()
    try:
        with Image.open("shirt.png") as shirt, Image.open(beforeimg) as muppet:
            width, height = shirt.size #get the size of the shirt
            muppet = ImageOps.fit(image=muppet,size=(width, height)) #resize/crop muppet to the size of shirt
            muppet.paste(shirt, (0, 0), shirt) #past shirt over muppet
            muppet.save(afterimg)
    except FileNotFoundError:
        sys.exit("File does not exist")

main()

