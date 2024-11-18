class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): #defines how an object is represented as a string when it is converted to one
        return f"{self.name} from {self.house}"
    
    def charm(self): #where specific cases have specific results
        match self.patronus: #if patronus exists
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus) #the class is being created and returned

def main():
    student = get_student() #student = the class from get_student()
    print(student) #display the class 
    #When print(student) is called, Python implicitly calls the __str__ method of the Student class
    print("Expecto Patronum!", student.charm())


if __name__ == "__main__":
    main()
