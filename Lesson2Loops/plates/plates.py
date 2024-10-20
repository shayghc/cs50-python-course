# This code was refactored from the code used in lesson 2
# The reason was to break the code out into functions with single responsibility in line with "clean code" guidelines
# This also facilitates more discrete unit testing

def main():
    """
    The main function of the program. It prompts the user to input a plate number,
    checks its validity using the `is_valid` function, and prints the result.

    Parameters:
    None

    Returns:
    None
    """
    # Side effects limited to main()
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    """
    Check if a given string represents a valid plate number according to specific rules.

    This function takes a string `s` as input and checks if it meets the following criteria:
    1. The length of the string is between 2 and 6 characters, inclusive.
    2. The first two characters are letters.
    3. The string does not contain any punctuation characters.
    4. There are no digits in the middle of the string.
    5. The first digit is not zero.

    Parameters:
    s (str): The input string to check. The length of the string should be at least 2 and at most 6.

    Returns:
    bool: True if the input string represents a valid plate number according to the specified rules.
          False otherwise.
    """
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
    """
    Check if the length of the given string is within the valid range for a plate.

    This function takes a string `s` as input and checks if its length is between 2 and 6 characters, inclusive.
    This is a precondition for checking the validity of a plate number according to the rules defined in the main function.

    Parameters:
    s (str): The input string to check. The length of the string should be at least 2 and at most 6.

    Returns:
    bool: True if the length of the string is within the valid range (2 to 6 characters), False otherwise.
    """
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True



def first_two_chars_are_letters(s):
    """
    Check if the first two characters of the given string are letters.

    This function takes a string `s` as input and checks if the first two characters are alphabetic.
    It also verifies that the string does not contain any punctuation characters.

    Parameters:
    s (str): The input string to check. The length of the string should be at least 2.

    Returns:
    bool: True if the first two characters are letters and the string does not contain any punctuation characters.
          False otherwise.
    """
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Check for punctuation
    for char in s:
        if char.isalpha() == False and char.isdigit() == False:
            return False



def numbers_not_in_middle(s):
    """
    Check if numbers are not in the middle of a plate.

    This function iterates through the given string `s` and identifies the positions of digits and letters.
    It then checks if any digit is found before the last letter. If such a case is found, the function returns False.
    Otherwise, it returns True.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if no digit is found before the last letter, False otherwise.
    """
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
    """
    Check if the first digit in the given string is not zero.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the first digit is not zero, False otherwise.
    """
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