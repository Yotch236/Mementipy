import os
from datetime import date, datetime


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_birthday():
    name = input("Enter the Celebrant Name: ").strip()
    dob = input("Enter the birthday of the celebrant [mm/dd/yyyy]: ").strip()

    try:
        bday_month, bday_day, bday_year = map(int, dob.split("/"))
        date(bday_year, bday_month, bday_day)  # validate date

        with open("birthday.txt", "a") as file:
            file.write(f"{name}, {dob}\n")
        print("✅ Birthday Celebrant Added Successfully.")
    except ValueError:
        print("❌ Invalid date. Use mm/dd/yyyy format and ensure it's a valid date.")


def list_birthdays():
    try:
        with open("birthday.txt", "r") as file:
            birthdays = [line.strip() for line in file.readlines()]
            if not birthdays:
                print("📭 No birthdays found.")
                return

        birthday_list = []
        for line in birthdays:
            parts = line.split(", ")
            if len(parts) == 2:
                name, dob = parts
                birthday_list.append((name, dob))
            else:
                print(f"⚠️ Skipping invalid entry: {line}")

        sort_choice = input("Sort by (1) Name, (2) Month, (3) Day, or (4) Year? [1/2/3/4]: ").strip()

        if sort_choice == "2":
            birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").month)
        elif sort_choice == "3":
            birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").day)
        elif sort_choice == "4":
            birthday_list.sort(key=lambda x: datetime.strptime(x[1], "%m/%d/%Y").year)
        else:
            birthday_list.sort(key=lambda x: x[0].lower())

        filter_choice = input("Do you want to filter birthdays? (y/n): ").lower()
        filtered_birthdays = birthday_list

        if filter_choice == 'y':
            filter_type = input("Filter by (1) Month, (2) Day, or (3) Year? [1/2/3]: ").strip()
            try:
                if filter_type == "1":
                    month_input = input("Enter month (MM): ").strip()
                    if not month_input.isdigit() or not (1 <= int(month_input) <= 12):
                        print("❌ Invalid month. Please enter a number between 1 and 12.")
                        return
                    month = int(month_input)
                    filtered_birthdays = [
                        b for b in birthday_list if datetime.strptime(b[1], "%m/%d/%Y").month == month
                    ]
                elif filter_type == "2":
                    day_input = input("Enter day (DD): ").strip()
                    if not day_input.isdigit() or not (1 <= int(day_input) <= 31):
                        print("❌ Invalid day. Please enter a number between 1 and 31.")
                        return
                    day = int(day_input)
                    filtered_birthdays = [
                        b for b in birthday_list if datetime.strptime(b[1], "%m/%d/%Y").day == day
                    ]
                elif filter_type == "3":
                    year_input = input("Enter year (YYYY): ").strip()
                    if not year_input.isdigit() or not (1000 <= int(year_input) <= 9999):
                        print("❌ Invalid year. Please enter a 4-digit year.")
                        return
                    year = int(year_input)
                    filtered_birthdays = [
                        b for b in birthday_list if datetime.strptime(b[1], "%m/%d/%Y").year == year
                    ]
                else:
                    print("Invalid filter choice.")
            except ValueError:
                print("❌ Invalid number input.")
                return

        if not filtered_birthdays:
            print("📭 No birthdays found matching your filter.")
        else:
            print("\n🎉 Celebrants List:")
            for name, dob in filtered_birthdays:
                print(f"🧑 {name}'s birthday is on {dob}")

    except FileNotFoundError:
        print("❌ No birthday file found. Please add a birthday first.")


def update_birthday_celebrant():
    try:
        with open("birthday.txt", "r") as file:
            birthday_list = [line.strip().split(", ") for line in file if line.strip()]
    except FileNotFoundError:
        print("❌ No birthday file found. Please add a birthday first.")
        return

    name_to_update = input("Enter the name of the celebrant to update: ").strip()

    found = False
    for i, (name, birthday) in enumerate(birthday_list):
        if name.lower() == name_to_update.lower():
            new_name = input("Enter the new name: ").strip()
            new_bday = input("Enter the new birthday [mm/dd/yyyy]: ").strip()
            try:
                datetime.strptime(new_bday, "%m/%d/%Y")  # validate date format
                birthday_list[i] = [new_name, new_bday]
                found = True
            except ValueError:
                print("❌ Invalid date format.")
            break

    if not found:
        print("❌ Celebrant not found.")
        return

    with open("birthday.txt", "w") as file:
        for entry in birthday_list:
            file.write(", ".join(entry) + "\n")
    print("✅ Birthday updated successfully.")


def delete_birthday_celebrant():
    try:
        with open("birthday.txt", "r") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("❌ The file does not exist.")
        return

    name_to_delete = input("Enter the exact name of the celebrant to delete: ").strip()

    updated_lines = [line for line in lines if not line.lower().startswith(name_to_delete.lower() + ",")]

    if len(updated_lines) == len(lines):
        print("❌ No matching celebrant found.")
        return

    with open("birthday.txt", "w") as f:
        for line in updated_lines:
            f.write(line + "\n")

    print(f"✅ {name_to_delete} has been deleted from the birthday list.")


def main():
    while True:
        clear_screen()
        print("----------------------------------")
        print("            MEMENTIPY")
        print("----------------------------------")
        print("           1. Add Birthday")
        print("           2. List All Birthdays")
        print("           3. Update Birthday")
        print("           4. Delete a Birthday Celebrant")
        print("           5. Exit")
        print("----------------------------------")

        try:
            choice = int(input("Enter choice [1-5]: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number 1-5.")
            input("Press Enter to continue...")
            continue

        if choice == 1:
            clear_screen()
            print("📝 ADD BIRTHDAY")
            add_birthday()
        elif choice == 2:
            clear_screen()
            print("📜 LIST ALL BIRTHDAYS")
            list_birthdays()
        elif choice == 3:
            clear_screen()
            print("✏️ UPDATE BIRTHDAY CELEBRANT")
            update_birthday_celebrant()
        elif choice == 4:
            clear_screen()
            print("🗑 DELETE BIRTHDAY CELEBRANT")
            delete_birthday_celebrant()
        elif choice == 5:
            print("👋 Exiting MementiPy. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

        if input("\nReturn To Menu [y/n]: ").lower() != "y":
            break


if __name__ == "__main__":
    main()
