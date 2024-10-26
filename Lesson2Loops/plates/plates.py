# This code was refactored from the code used in lesson 2
# The reason was to abstract the code out into helper functions with single responsibility in line with "clean code" guidelines
# This also facilitates more discrete unit testing

def main():
    # Main function to prompt user input and validate the license plate.
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Validate the vanity plate according to the specified requirements.
    return (check_plate_length(s) 
            and first_two_chars_are_letters(s) 
            and numbers_not_in_middle(s)
            and no_punctuation(s))


def check_plate_length(s):
    Check if the string length is between 2 and 6 characters.
    return 2 <= len(s) <= 6


def first_two_chars_are_letters(s):
    # Check if the string starts with at least two letters.
    return s[:2].isalpha()


def numbers_not_in_middle(s):
    # Check if numbers (if any) are at the end of the string and no letters appear after them.
    found_digit = False  # Flag to indicate if a digit has been found
    for char in s:
        if char.isdigit():
            # If we encounter a digit, we set the found_digit flag
            found_digit = True
            # The first digit must never be '0'
            if char == '0':
                return False
        elif found_digit:
            # If we've found a digit, there should be no letters after it
            if char.isalpha():
                return False
    return True

def no_punctualtion(s):
    # Check that all characters in the string are alpha or digit - no punctuation
    return s.isalnum()


if __name__ == "__main__":
    main()