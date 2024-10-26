menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def get_item():
    while True:
        try:
            item=input("Item: ").strip().title()
            if item in menu:
                return menu[item]
            else:
                continue
        except EOFError:
            break

def get_price():
    cost=0
    while True:
        price=get_item()
        if price is None:
            break
        cost+=price
        total=(f"Total: ${cost:.2f}")
        print(total)
        #No need for return: The function doesn’t need to pass any value to others

get_price()


