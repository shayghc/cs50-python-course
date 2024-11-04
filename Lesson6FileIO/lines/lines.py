"""In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank."""

import sys


def main() -> None:
    """
    The main function of the program. It counts the number of lines of code in a specified Python file, excluding comments and blank lines.

    Parameters:
    None

    Returns:
    None

    The function performs the following steps:
    1. Initiates a count variable to 0.
    2. Validates the command line arguments using the validate_arguments function. If the arguments are not valid, the program exits.
    3. Tries to open the specified file in read mode. If the file does not exist, the program exits with an appropriate error message.
    4. Reads all lines from the file.
    5. Iterates over each line, checking if it is a comment or a blank line. If it is not, increments the count variable.
    6. Prints the final count of lines of code.
    """
    # Initiate count
    count = 0
    # Check that arguments are correct
    if not validate_arguments(sys.argv):
        sys.exit()

    # Try to open the file
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    for line in lines:
        if line.lstrip().startswith("#") or line.isspace():
            continue
        else:
            count += 1
    print(count)



def validate_arguments(args: list) -> bool:
    """
    Validates the command line arguments for the Python file.

    Args:
        args (list): A list of command line arguments. The first argument is the script name, and the second argument is the file name.

    Returns:
        bool: True if the arguments are valid, False otherwise. If the arguments are invalid, the program will exit with an appropriate error message.
    """
    # Check if command line args are valid
    if len(args) != 2:
        if len(args) < 2:
            sys.exit("Too few command line arguments")
        else:
            sys.exit("Too many command line arguments")

    if not args[1].endswith(".py"):
        sys.exit("Not a Python file!")

    return True



if __name__ == "__main__":
    main()
