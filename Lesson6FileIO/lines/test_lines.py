"""In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank."""

import sys


def main():
    count = 0

    if check_file(sys.argv) == "Valid":
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            for line in lines:
                if line.lstrip().startswith("#") or line.isspace():
                    continue
                else:
                    count += 1
            print(count)


# Check that sys.argv is the right length and that the file exists
def check_file(file):
    if len(file) < 2:
        sys.exit("Too few command-line arguments")
    elif len(file) > 2:
        sys.exit("Too many command-line arguments")
    elif not file[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return "Valid"


if __name__ == "__main__":
    main()