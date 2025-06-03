import datetime
from win10toast_click import ToastNotifier

toaster = ToastNotifier()
ICON_PATH = None  # Set your custom icon path here if needed

def load_bdays(file_path):
    birthdays = {}
    try:
        with open(file_path, "r") as f:
            for line in f:
                name, dob = map(str.strip, line.strip().split(","))
                dob_datetime = datetime.datetime.strptime(dob, "%m/%d/%Y")
                dob_month_day = (dob_datetime.month, dob_datetime.day)
                year_of_birth = dob_datetime.year
                if dob_month_day in birthdays:
                    birthdays[dob_month_day].append((name, year_of_birth))
                else:
                    birthdays[dob_month_day] = [(name, year_of_birth)]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print("An error occurred:", e)
    return birthdays

def notify_next_celebrant(birthdays):
    today = datetime.date.today()
    current_year = today.year
    days_ahead = 1

    while days_ahead <= 366:  # Max search window: 1 year
        future_day = today + datetime.timedelta(days=days_ahead)
        key = (future_day.month, future_day.day)

        if key in birthdays:
            celebrants = birthdays[key]
            names = ', '.join(name for name, _ in celebrants)
            ages = ', '.join(str(current_year - year_of_birth) for _, year_of_birth in celebrants)

            date_str = future_day.strftime("%B %d")
            message = (
                f"Next birthday: {names} on {date_str} "
                f"and turning {' & '.join(ages.split(', '))} years old."
            )

            toaster.show_toast("Upcoming Celebrant", message, icon_path=ICON_PATH, duration=10, threaded=True)
            break

        days_ahead += 1

def check_bdays(birthdays):
    today = datetime.date.today()
    current_year = today.year
    today_month_day = (today.month, today.day)
    
    if today_month_day in birthdays:
        celebrants = birthdays[today_month_day]
        if len(celebrants) > 1:
            the_title = "Mementipy Notification"
            message = "The following celebrants share this birthday today:\n"
            for name, year_of_birth in celebrants:
                age = current_year - year_of_birth
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(age % 10, "th") if age % 100 not in {11, 12, 13} else "th"
                message += f"{name} ({age}{suffix} years old)\n"
        else:
            name, year_of_birth = celebrants[0]
            age = current_year - year_of_birth
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(age % 10, "th") if age % 100 not in {11, 12, 13} else "th"
            the_title = "Mementipy Notification"
            message = f"Happy {age}{suffix} Birthday to {name} today!!"
        toaster.show_toast(title=the_title, msg=message, icon_path=ICON_PATH, duration=10, threaded=True)
    else:
        notify_next_celebrant(birthdays)

# Example usage
birthdays = load_bdays("birthday.txt")
check_bdays(birthdays)
