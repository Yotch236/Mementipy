import os
from datetime import date, datetime


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_birthday():
    name = input("Enter the Celebrant Name: ")
    dob = input("Enter the birthday of the celebrant [mm/dd/yyyy]: ")

    try:
        bday_month, bday_day, bday_year = map(int, dob.split("/"))
        # Check if the date is valid
        date(bday_year, bday_month, bday_day)

        with open("birthday.txt", "a") as file:
            file.write(f"{name}, {dob}\n")
            print("Added Birthday Celebrant Successfully")
    except ValueError:
        print("Invalid date. Please use mm/dd/yyyy format and ensure it's a real date.")


def list_birthdays():
    try:
        with open("birthday.txt", "r") as file:
            birthdays = file.readlines()
            if not birthdays:
                print("No birthdays found.")
                return
            
            # Parse and sort birthdays
            birthday_list = []
            for line in birthdays:
                parts = line.strip().split(", ")
                if len(parts) == 2:
                    name, dob = parts
                    birthday_list.append((name, dob))
                else:
                    print("Invalid entry format in file")

            birthday_list.sort(key=lambda x: x[0])  # Sort by name

            # Option to filter by date
            filter_date = input("Do you want to filter by date [mm/dd]? (Press Enter to skip): ")
            if filter_date:
                try:
                    filter_month, filter_day = map(int, filter_date.split("/"))
                    filtered_birthdays = [
                        (name, dob) for name, dob in birthday_list 
                        if datetime.strptime(dob, "%m/%d/%Y").month == filter_month and
                           datetime.strptime(dob, "%m/%d/%Y").day == filter_day
                    ]
                except ValueError:
                    print("Invalid date format. Please use mm/dd format.")
                    return
            else:
                clear_screen()
                filtered_birthdays = birthday_list

            # Display birthdays
            if not filtered_birthdays:
                print("No birthdays found for the given date.")
            else:
                for name, dob in filtered_birthdays:
                    print(f"{name}'s birthday is on {dob}")
    except FileNotFoundError:
        print("No birthday file found. Please add a birthday first.")

def Delete_Birthday_Celebrant():
    try:
        with open("birthday.txt", "r") as file:
            lines = file.readlines()


        celebrant_name_todelete = input("Enter the name of the birthday celebrant to delete:")

        with open("birthday.txt", "w") as f:
            for line in lines:
                if celebrant_name_todelete not in line:
                    f.write(line)
        print(f"{celebrant_name_todelete} has been deleted from the birthday list")

    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print("An error occurred:", e)            


def main():
    while True:
        clear_screen()
        print("----------------------------------")
        print("            MEMENTIPY")
        print("----------------------------------")
        print("           1. Add Birthday")
        print("           2. List All Birthdays")
        print("           3. Delete an Birthday Celebrant ")
        print("           4. Exit")
        print("----------------------------------")

        try:
            choice = int(input("Enter choice [1-4]: "))
        except ValueError:
            print("Invalid input. Please enter a number 1-4.")
            input("Press Enter to continue...")
            continue

        if choice == 1:
            clear_screen()
            print("------------------------------")
            print("        ADD BIRTHDAY")
            print("------------------------------")
            add_birthday()
            if input("Return To Menu [y/n]: ").lower() != "y":
                break
        elif choice == 2:
            clear_screen()
            print("----------------------------")
            print("    LIST ALL BIRTHDAYS")
            print("----------------------------")
            list_birthdays()
            print("----------------------------")
            if input("Return To Menu [y/n]: ").lower() != "y":
                break
        elif choice == 3:
            clear_screen()
            print("-----------------------------")
            print("  DELETE BIRTHDAY CELEBRANT")
            print("-----------------------------")
            Delete_Birthday_Celebrant()
            print("-----------------------------")
            if input("Return To Menu [y/n]: ").lower()!= "y":
                break
        elif choice == 4:
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()