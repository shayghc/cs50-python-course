"""
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
"""

import re

C:\Users\sghco\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts
def main():
    """
    The main function is the entry point of the program.
    It prompts the user to input an IPv4 address, validates it using the validate function,
    and then prints the result.

    Parameters:
    None

    Returns:
    None
    """
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Validates if a given string is a valid IPv4 address.

    Parameters:
    ip (str): The string to be validated. It should be a string representation of an IPv4 address.

    Returns:
    bool: True if the input string is a valid IPv4 address, False otherwise.
    """
    return bool(
        re.search(
            r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)$",
            ip,
        )
    )


if __name__ == "__main__":
    main()