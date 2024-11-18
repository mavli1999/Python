import random

class Hat:
    def __init__(self): #for when a new instance of the class is initiated
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):#sort is a function within the Hat class.
        print(name, "is in", random.choice(self.houses))

hat = Hat() #define one instance of the class Hat; only possible with __init_
hat.sort("Harry") #sort is a function within the Hat class.
