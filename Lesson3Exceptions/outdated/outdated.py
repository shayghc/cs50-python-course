import re


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
        "December",
    ]

    while True:
        # Get user date input in MM/DD/YYYY or Month DD, YYYY format
        user_date = input(
            "Enter a date in 'MM/DD/YYYY' or 'Month DD, YYYY' format: "
        ).strip()

        # Regex pattern to match 'MM/DD/YYYY' or 'Month DD, YYYY' formats
        """Regex Pattern (pattern):
        1. ^\d{1,2}/\d{1,2}/\d{4}$: Matches the MM/DD/YYYY format.
        2. |: Combines the two formats with an OR operator.
        3. ^(January|February|...|December) \d{1,2}, \d{4}$: Matches the Month DD, YYYY format.
        """
        pattern = r"^\d{1,2}/\d{1,2}/\d{4}$|^(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}$"
        if not re.match(pattern, user_date):
            continue  # Exit the loop if the format does not match

        # Process the date by replacing delimiters and splitting into month, day, year
        month, day, year = user_date.replace("/", " ").replace(",", " ").split()

        # Check our exceptions
        try:
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        else:
            # If the month is in months_list, then it is obviously an alpha value
            if month.lower().capitalize() in months_list:
                month = months_list.index(month) + 1
            elif month.isnumeric():
                month = int(month)

        if day > 31 or month > 12:
            continue

        # Print ISO 8601 format date
        print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
        break


if __name__ == "__main__":
    main()
