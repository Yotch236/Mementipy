import datetime
from win10toast import ToastNotifier

toaster = ToastNotifier()

def load_bdays(file_path):
    birthdays = {}
    current_year = datetime.datetime.now().year #Get the current year
    with open(file_path, "r") as f:
        for line in f:
            name, dob = line.strip().split(",")
            name = name.strip()
            dob = dob.strip()
            dob_with_year = f"{dob}/{current_year}"
            dob_datetime = datetime.datetime.strptime(dob_with_year, "%m/%d/%Y")
            dob_month_day = (dob_datetime.month, dob_datetime.day)
            if dob_month_day in birthdays:
                birthdays[dob_month_day].append(name)
            else:
                birthdays[dob_month_day] = [name]
    return birthdays

def check_bdays(birthdays):
    today = datetime.date.today()
    today_month_day = (today.month, today.day)
    if today_month_day in birthdays:
        celebrants = birthdays[today_month_day]
        if len(celebrants) > 1:
            the_title = "Mementipy Notification"
            message = f"The following celebrants share the birthday today:\n"
            for name in celebrants:
                message += f"{name}\n"
        else:
            the_title = "Mementipy Notification"
            message = f"Happy Birthday to {celebrants[0]} today!!"
        toaster.show_toast(title=the_title, msg=message, duration=10)

birthdays = load_bdays("birthday.txt")
check_bdays(birthdays)
