import re


def main():
    """
    This function is the entry point of the program. It prompts the user to input an IPv4 address,
    validates it using the validate function, and prints the result.

    Parameters:
    None

    Returns:
    None
    """
    print(validate(input("IPv4 Address: ")))


def validate(ip):
        """
    Validates an IPv4 address.

    This function takes a string representing an IPv4 address as input and checks if it is a valid IPv4 address.
    It uses regular expressions to match the input against the pattern of an IPv4 address. If the input matches the pattern,
    it further checks if each octet of the address is within the valid range of 0 to 255.

    Parameters:
    ip (str): A string representing an IPv4 address.

    Returns:
    bool: True if the input is a valid IPv4 address, False otherwise.
    """
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        try:
            octet1 = int(matches.group(1))
            octet2 = int(matches.group(2))
            octet3 = int(matches.group(3))
            octet4 = int(matches.group(4))
            if (
                0 <= octet1 <= 255
                and 0 <= octet2 <= 255
                and 0 <= octet3 <= 255
                and 0 <= octet4 <= 255
            ):
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False


if __name__ == "__main__":
    main()