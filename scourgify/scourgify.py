import sys
import csv

def user_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >3:
        sys.exit("Too many command-line arguments")
    else:
        before_file = sys.argv[1]
        after_file = sys.argv[2]
        return before_file, after_file

def main():
    before_file, after_file = user_input()
    try:
        with open(before_file, "r") as before, open(after_file,"w") as after:
            reader = csv.reader(before) #automatically turn each row into a list of values
            writer = csv.DictWriter(after, fieldnames=["first"] + ["last"] + ["house"])
            writer.writeheader()
            next(reader) #skip the header row of the reader file

            for row in reader:
                name, house = row #assign each values from the list of each row
                last_name, first_name = name.split(", ")

                writer.writerow({
                    "first": first_name, #dont need to row[] before it's already assigned to first_name
                    "last": last_name,
                    "house": house
                })
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
