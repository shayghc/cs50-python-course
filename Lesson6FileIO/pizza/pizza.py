"""In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library's grid format. If the user does not specify exactly one command-line argument, or if the specified file's name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit."""

import sys
import csv
import os
from tabulate import tabulate


def main() -> None:
    # Get table data
    if not check_file(sys.argv):
        return

    # Initialise the table
    table = []

    # Try to open the csv file
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                if len(row) < len(headers):
                    continue  # Skips rows with insufficient data
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Display the result
    print(tabulate(table, headers=headers, tablefmt="grid"))


def check_file(file: list) -> bool:
    if len(file) != 2:
        sys.exit("Usage: python pizza.py <filename>.csv")
    elif not file[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not os.path.isfile(file[1]):
        sys.exit("File does not exit")
    return True


if __name__ == "__main__":
    main()
