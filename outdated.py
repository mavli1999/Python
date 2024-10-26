monthlist = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def exception():
    while True:
        dateinput=input("Date: ").strip()

        try: #try excpet works like if not; you can use excpet as if not, then .....
            month_num, day, year = dateinput.split('/')
            month_num, day, year = int(month_num), int(day), int(year)
            #see if they can be converted to int

        except ValueError: #if they cant be converted to int
            if ',' not in dateinput or not dateinput[0].isalpha():
                continue

            dateinput = dateinput.replace(',','').lower()
            month, day, year = dateinput.split()
            month = month.capitalize()

            if month in monthlist:
                month_num = monthlist.index(month)+1
            else:
                continue

            month_num, day, year = int(month_num), int(day), int(year)

        #return everything here
        if 1 <= month_num <= 12 and 1 <= day <= 31:
            return month_num, day, year

def main(): # dont need a while loop because it's already happened in exception()
    month_num, day, year = exception()
    month_num = str(month_num).zfill(2)
    day = str(day).zfill(2)
    print(f"{year}-{month_num}-{day}")

main()
