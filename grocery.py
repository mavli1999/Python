grocery={}

def grocery_list():

    try:
        while True:
            item=input().strip().lower()

            if item in grocery:
                grocery[item]+=1
            else:
                grocery[item]=1

    except EOFError:
        pass

    return grocery #return at the end outside the loop; if return in the mid of loop it'll exit the loop

def main():
    #have to collect the items first
    grocery=grocery_list()

    for item in sorted(grocery):
        print(f"{grocery[item]} {item.upper()}")

main()
