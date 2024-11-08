import sys
from tabulate import tabulate
import csv

table = []

def user_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.csv'):
        sys.exit("Not a CSV file")
    else:
        filename = sys.argv[1]
        return filename

def main():
    table = []
    filename = user_input()
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            #headers = reader.fieldnames
            for row in reader:
                table.append(row) #append row to the table list
            print(tabulate(table, headers="keys", tablefmt="grid")) #use the keys of the table list as headers
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
