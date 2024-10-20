# This code was refactored from the code used in lesson 2
# The reason was to break the code out into functions with single responsibility in line with "clean code" guidelines
# This also facilitates more discrete unit testing

def main():
    # Side effects limited to main()
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        check_plate_length(s) == False
        or first_two_chars_are_letters(s) == False
        or numbers_not_in_middle(s) == False
        or first_digit_not_zero(s) == False
    ):
        return False
    else:
        return True


def check_plate_length(s):
    # Check plate length
    # Need to check minimum length before checking first two characters are letters
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True


def first_two_chars_are_letters(s):
    # Check that first two characters are letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Check for punctuation
    for char in s:
        if char.isalpha() == False and char.isdigit() == False:
            return False


def numbers_not_in_middle(s):
    # Check numbers are not in the middle of a plate
    digit_positions = []
    letter_positions = []
    for char in s:
        if char.isdigit():
            digit_positions.append(s.index(char))
        elif char.isalpha():
            letter_positions.append(s.index(char))
    if len(digit_positions) > 0 and len(letter_positions) > 0:
        if int(digit_positions[0]) < int(letter_positions[-1]):
            return False


def first_digit_not_zero(s):
    # Check that the first digit is not a zero
    for char in s:
        # This code will not work without including this first condition to continue for alpha chars
        if char.isalpha():
            continue
        elif char.isdigit() and char == "0":
            return False
        else:
            return True


if __name__ == "__main__":
    main()