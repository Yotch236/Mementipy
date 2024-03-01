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
            dob  = dob.strip()
            dob_with_year = f"{dob}/{current_year}"
            birthdays[name] = datetime.datetime.strptime(dob_with_year, "%m/%d/%Y")
    return birthdays
            

def check_bdays(birthdays):
    today = datetime.date.today()
    for name,dob in birthdays.items():
        if dob.month == today.month and dob.day == today.day:
            the_title = "Mementipy Notification"
            message = f"It's {name} birthday today!"
            toaster.show_toast(title = the_title, msg = message, duration = 3)

birthdays = load_bdays("birthday.txt")
check_bdays(birthdays)