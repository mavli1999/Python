#returning but not printing
def check():
    answer=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
    if answer.lower() == "forty-two" or answer.lower() == "forty two":
        return "yes"
    elif answer.isdigit() and int(answer) == 42:
        return "yes"
    else:
        return "no"

#print out the returned results
def main():
    result=check()
    print(result)

main()
