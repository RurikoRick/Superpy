import csv
from datetime import datetime, timedelta

now = datetime.now()

def advanced(number):
    # open the datefile
    with open ("date_advance.csv", "r") as file:
        reader = csv.reader(file)
        date = datetime.strftime(now, "%Y-%m-%d")
        for row in reader:
            date = row[0]
    
    # change the date into a date object WITH time (00:00:00)
    new_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=number)
    # rechance the date into a string object WITHOUT time (00:00:00)
    new_date = datetime.strftime(new_date, "%Y-%m-%d")

    # overwrite the row with the newdate
    with open ("date_advance.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([new_date])

def setdate(new_date):
    date = datetime.strftime(now, "%Y-%m-%d")
    # chance the date entirely
    if new_date == "today":
        with open ("date_advance.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date])
    else:
        with open ("date_advance.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_date])
