import os
from datetime import date


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
            for line in birthdays:
                parts = line.strip().split(", ")
                if len(parts) == 2:
                    name, dob = parts
                    print(f"{name}'s birthday is on {dob}")
                else:
                    print("Invalid entry format in file")
    except FileNotFoundError:
        print("No birthday file found. Please add a birthday first.")


def main():
    while True:
        clear_screen()
        print("----------------------------------")
        print("            MEMENTIPY")
        print("----------------------------------")
        print("           1. Add Birthday")
        print("           2. List All Birthdays")
        print("           3. Exit")
        print("----------------------------------")

        try:
            choice = int(input("Enter choice [1-3]: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
