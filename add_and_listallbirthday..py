import os
from datetime import date, datetime


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def write_entry(file, name, dob):
    file.write(f"{name}, {dob}\n")


def add_birthday():
    name = input("Enter the Celebrant Name: ").strip()
    dob = input("Enter the birthday [mm/dd/yyyy]: ").strip()

    try:
        datetime.strptime(dob, "%m/%d/%Y")  # validate date
        with open("birthday.txt", "a") as file:
            write_entry(file, name, dob)
        print("Added Birthday Celebrant Successfully")
    except ValueError:
        print("Invalid date format. Please use mm/dd/yyyy.")


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
                    birthday_list.append((parts[0], parts[1]))

            sort_choice = input(
                "Sort by (1) Name, (2) Month, (3) Day, (4) Year? [1/2/3/4]: "
            )

            if sort_choice == "2":
                birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").month)
            elif sort_choice == "3":
                birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").day)
            elif sort_choice == "4":
                birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").year)
            else:
                birthday_list.sort(key=lambda x: x[0].lower())

            # filtering
            if input("Do you want to filter birthdays? (y/n): ").lower() == 'y':
                filter_type = input("Filter by (1) Month, (2) Day, (3) Year? [1/2/3]: ")

                try:
                    if filter_type == "1":
                        m = int(input("Enter month (MM): "))
                        birthday_list = [b for b in birthday_list
                                         if datetime.strptime(b[1], "%m/%d/%Y").month == m]
                    elif filter_type == "2":
                        d = int(input("Enter day (DD): "))
                        birthday_list = [b for b in birthday_list
                                         if datetime.strptime(b[1], "%m/%d/%Y").day == d]
                    elif filter_type == "3":
                        y = int(input("Enter year (YYYY): "))
                        birthday_list = [b for b in birthday_list
                                         if datetime.strptime(b[1], "%m/%d/%Y").year == y]
                except ValueError:
                    print("Invalid number input.")
                    return

            if not birthday_list:
                print("No birthdays found.")
            else:
                for name, dob in birthday_list:
                    print(f"{name}'s birthday is on {dob}")

    except FileNotFoundError:
        print("No birthday file found. Add a birthday first.")


def UpdateBdayCelebrant():
    try:
        with open("birthday.txt", "r") as file:
            birthday_list = [line.strip().split(", ") for line in file]
    except FileNotFoundError:
        print("No birthday file found. Please add a birthday first.")
        return

    name_to_update = input("Enter the name to update: ").strip()

    for i, (name, dob) in enumerate(birthday_list):
        if name.lower() == name_to_update.lower():
            new_name = input("Enter new name: ").strip()
            new_dob = input("Enter new birthday [mm/dd/yyyy]: ").strip()

            try:
                datetime.strptime(new_dob, "%m/%d/%Y")
            except ValueError:
                print("Invalid date format.")
                return

            birthday_list[i] = [new_name, new_dob]
            break
    else:
        print("Celebrant not found.")
        return

    with open("birthday.txt", "w") as file:
        for name, dob in birthday_list:
            write_entry(file, name, dob)

    print("Birthday updated successfully.")


def Delete_Birthday_Celebrant():
    try:
        with open("birthday.txt", "r") as file:
            lines = file.readlines()

        name_to_delete = input("Enter the name to delete: ").strip().lower()

        with open("birthday.txt", "w") as file:
            deleted = False
            for line in lines:
                name, dob = line.strip().split(", ")
                if name.lower() != name_to_delete:
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print(f"{name_to_delete} has been deleted.")
        else:
            print("Celebrant not found.")

    except FileNotFoundError:
        print("No birthday file found.")


def main():
    while True:
        clear_screen()
        print("----------------------------------")
        print("            MEMENTIPY")
        print("----------------------------------")
        print("1. Add Birthday")
        print("2. List All Birthdays")
        print("3. Update Birthday")
        print("4. Delete Birthday Celebrant")
        print("5. Exit")
        print("----------------------------------")

        choice = input("Enter choice [1-5]: ")

        if choice == "1":
            clear_screen()
            add_birthday()
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            clear_screen()
            list_birthdays()
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            clear_screen()
            UpdateBdayCelebrant()
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            clear_screen()
            Delete_Birthday_Celebrant()
            input("\nPress Enter to return to menu...")
        elif choice == "5":
            break
        else:
            print("Invalid input.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
