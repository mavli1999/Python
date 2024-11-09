import numpy as np
import csv
from PIL import Image

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

def main(): 
    with open("views.csv", "r") as views, open("analysis.csv","w") as analysis:
        reader = csv.DictReader(views) #reads each row as an ordered dictionary
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"]) 
        #this new file called analysis will have the same headers as the views file + brightness

        writer.writeheader() #write out the header in analysis file

        for row in reader:
            brightness = calculate_brightness(f"{row["id"]}.jpeg")
            writer.writerow({ 
                "id": row["id"], #the id column will have row["id"] from the views file
                "english_title": row["english_title"], 
                "japanese_title": row["japanese_title"],
                "brightness": round(brightness,2)
            }) #add to analysis file

            #or use the simplied below:
            #row["brightness"]=calculate_brightness(f"{row["id"]}.jpeg") - create a new row based on view file
            #writer.writerow(row) - then add all columns to writer file 
    



main()
