#create folder with today's date
import os
import datetime
date_today = datetime.date.today()
folder = date_today.strftime('%Y-%m-%d')
if not os.path.exists(folder):
    os.makedirs(folder)

folder = date_today

#Input screen
name = input("Enter your name: ")
surname = input("Enter your surname: ")
id_number = input ("Enter your ID number: ")

personal_file = input(f"{id_number}.txt")

# saving the information to the file
with open(folder, 'w') as f:
    f.write(f"name: {name}\n")
    f.write(f"surname: {surname}\n")
    f.write(f"id number: {id_number}\n")









