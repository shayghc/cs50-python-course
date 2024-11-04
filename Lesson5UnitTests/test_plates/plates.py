# This code was refactored from the code used in lesson 2
# The reason was to abstract the code out into helper functions with single responsibility in line with "clean code" guidelines
# This also facilitates more discrete unit testing


def main() -> None:
    # Main function to prompt user input and validate the license plate.
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    # Validate the vanity plate according to the specified requirements.
    return (
        check_plate_length(s)
        and first_two_chars_are_letters(s)
        and numbers_not_in_middle(s)
        and no_punctuation(s)
    )


def check_plate_length(s: str) -> bool:
    # Check if the string length is between 2 and 6 characters.
    return 2 <= len(s) <= 6


def first_two_chars_are_letters(s: str) -> bool:
    # Check if the string starts with at least two letters.
    return s[:2].isalpha()


def numbers_not_in_middle(s: str) -> bool:
    found_digit = False  # Flag to indicate if a digit has been found
    first_digit = True  # Flag to check if this is the first digit

    for char in s:
        if char.isdigit():
            if first_digit and char == "0":
                return False  # The first digit should not be '0'
            found_digit = True
            first_digit = (
                False  # Now that we've found a digit, it's not the first anymore
            )
        elif found_digit and char.isalpha():
            return False  # Letters should not appear after digits

    return True  # All checks passed


def no_punctuation(s: str) -> bool:
    # Check that all characters in the string are alpha or digit - no punctuation
    return s.isalnum()


if __name__ == "__main__":
    main()
