import datetime
from win10toast import ToastNotifier


toaster = ToastNotifier()

def load_bdays(file_path):
    birthdays = {}
    with open(file_path, "r") as f:
        for line in f:
            name, dob = line.strip().split(",")
            name = name.strip()
            dob = dob.strip()
            birthdays[name] = datetime.datetime.strptime(dob, "%m/%d")
    return birthdays

def check_bdays(birthdays):
    today = datetime.date.today()
    for name,dob in birthdays.items():
        if dob.month == today.month and dob.day == today.day:
            the_title = "Birthify Notification"
            message = f"It's {name} birthday today!"
            toaster.show_toast(title = the_title, msg = message, duration = 10)

birthdays = load_bdays("birthday.txt")
check_bdays(birthdays)