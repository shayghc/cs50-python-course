from datetime import date, datetime
import re
import sys
import inflect

p = inflect.engine()


def main():
    """
    The main function of the program.

    This function prompts the user to enter their date of birth, validates the input,
    calculates the equivalent number of minutes, and prints the result.

    Parameters:
    None

    Returns:
    None
    """
    try:
        birthdate = get_dob(input("Date of Birth: "))
    except:
        sys.exit("Invalid Date")
    print(minutes_to_text(birthdate))



def get_dob(dob):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", dob):
        return dob
    else:
        raise ValueError


def minutes_to_text(dob):
    """Converts a date of birth in YYYY-MM-DD format to the equivalent number of minutes.

    Parameters
    ----------
    dob : str
        The date of birth in YYYY-MM-DD format.

    Returns
    -------
    str
        The equivalent number of minutes represented in human-readable form.
    """
    birthdate = datetime.strptime(dob, "%Y-%m-%d").date()
    today = date.today()
    difference = today - birthdate
    difference_in_minutes = difference * 24 * 60
    difference_in_words = p.number_to_words(difference_in_minutes.days, andword="")
    return difference_in_words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
