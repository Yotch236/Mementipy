import os
from datetime import date

def add_birthday():
    name =  input("Enter the Celebrant Name:")
    dob= input("Enter the birthday of the celebrant[mm/dd]:")

    try:
        bday_month , bday_day = map(int, dob.split("/"))
        if bday_month in [1,3,5,7,8,10,12]:
            max_days = 31
        elif bday_month in [4,6,9,11]:
            max_days = 30
        else:
            max_days = 29 if date.today().year % 4 == 0 else 28

        if bday_month < 1 or bday_month > 12:
            print("Invalid Month Being Entered")
        elif bday_day < 1 or bday_day > max_days:
            print("Invalid Date Being Entered")
        else:
            with open('birthday.txt', "a") as file:
                file.write(f"{name}, {dob}\n")
                print("Added Birthday Celebrant Successfully")
    except ValueError:
        print("Invalid date format. Please use mm/dd format.")

def list_birthdays():
    with open("birthday.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                name, dob = parts
                print(f"{name} birthday is on {dob}")
            else:
                print("Invalid date format in file")


while(True):
    print("----------------------------------")
    print("            MEMENTIPY")
    print("----------------------------------")
    print("           1. Add Birthday")
    print("           2. List All Birthdays")
    print("           3. Exit")
    print("----------------------------------")
    ch = int(input("  Enter choice[1-3]:"))

    if ch == 1:
        os.system("cls")
        print("------------------------------")
        print("        ADD BIRTHDAY")
        print("------------------------------")
        add_birthday()
        if input("Return To Menu[y/n]:") !='y':
            break
            os.system("cls")
    elif ch == 2:
        os.system("cls")
        print("----------------------------")
        print("    LIST ALL BIRTHDAY")
        print("-----------------------------")
        list_birthdays()
        print("-----------------------------")
        if input("Return To Menu[y/n]:") !='y':
            break
            os.system("cls")
    elif ch == 3:
        os._exit(0)
    else:
        print("Invalid input. Please Enter [1-3]")
        if input("Return To Menu[y/n]:") !='y':
            break
            os.system("cls")

    