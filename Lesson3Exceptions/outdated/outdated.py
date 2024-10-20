"""
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

def main():
# Refactored

    months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        # Get user date input in MM-DD-YYYY format
        # Capturing the entire string initially allows us to perform checks for reject conditions
        user_date = input("Date:").strip()
        month, day, year = user_date.replace("/", " ").replace(",", "").split(" ")
        # This line is not required for the problem set but will correct any month input with a different case than the months in the list
        month = month.lower().capitalize()

        # Check for reject conditions
        if day.isalpha():
            continue
        elif month.isdigit() and 0 < int(month) > 12:
            continue
        elif month.isalpha() and "/" in user_date:
            continue
        elif month.isalpha() and "," not in user_date:
            continue
        # This condition is not required for the problem set however a user could enter an alpha value other than a month in months list
        elif month.isalpha() and month not in months_list:
            continue
        else:
            # Check our exceptions
            try:
                day = int(day)
                year = int(year)
                # This reject condition is placed here to check "day" and "year" after exception check for a ValueError
                # We want to ensure that they are "int" values before checking they are in a valid range
                if day < 1 or day > 31 or year < 1:
                    continue
            except ValueError:
                break
            else:
                # If month is in months_list then it is obviously an alpha value
                if month in months_list:
                    month = months_list.index(month) + 1
                elif month.isnumeric():
                    month = int(month)

        # Print ISO 8601 format date
        print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
        # This break corrects the "....\r\n..." failure seen check50 tests
        break

main()