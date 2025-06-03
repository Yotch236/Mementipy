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

            birthday_list = []
            for line in birthdays:
                parts = line.strip().split(", ")
                if len(parts) == 2:
                    name, dob = parts
                    birthday_list.append((name, dob))
                else:
                    print("Invalid entry format in file")

            # Choose sorting option
            sort_choice = input("Sort by (1) Name, (2) Month, (3) Day, or (4) Year? [1/2/3/4]: ")

            if sort_choice == "2":
                # Sort by month
                birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").month)
            elif sort_choice == "3":
                # Sort by day
                birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").day)
            elif sort_choice == "4":
                # Sort by year
                birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").year)
            else:
                # Default to sorting by name
                birthday_list.sort(key=lambda x: x[0])

            # Option to filter by date
            filter_choice = input("Do you want to filter birthdays? (y/n): ").lower()
            if filter_choice == 'y':
                filter_type = input("Filter by (1) Month, (2) Day, or (3) Year? [1/2/3]: ")
                filtered_birthdays = []

                if filter_type == "1":
                    try:
                        filter_month = int(input("Enter month (MM): "))
                        filtered_birthdays = [
                            (name, dob) for name, dob in birthday_list
                            if datetime.strptime(dob, "%m/%d/%Y").month == filter_month
                        ]
                    except ValueError:
                        print("Invalid month format. Please enter a number.")
                        return
                elif filter_type == "2":
                    try:
                        filter_day = int(input("Enter day (DD): "))
                        filtered_birthdays = [
                            (name, dob) for name, dob in birthday_list
                            if datetime.strptime(dob, "%m/%d/%Y").day == filter_day
                        ]
                    except ValueError:
                        print("Invalid day format. Please enter a number.")
                        return
                elif filter_type == "3":
                    try:
                        filter_year = int(input("Enter year (YYYY): "))
                        filtered_birthdays = [
                            (name, dob) for name, dob in birthday_list
                            if datetime.strptime(dob, "%m/%d/%Y").year == filter_year
                        ]
                    except ValueError:
                        print("Invalid year format. Please enter a number.")
                        return
                else:
                    print("Invalid filter choice.")
                    filtered_birthdays = birthday_list # Show all if invalid filter choice
            else:
                filtered_birthdays = birthday_list


            # Display birthdays
            if not filtered_birthdays:
                print("No birthdays found matching your filter.")
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