"""
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

There should be two functions inside main: convert and gauge:
convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""


def main() -> None:
    while True:
        # Prompt user for a fraction
        user_input = input("Enter fraction of fuel (X/Y): ").strip()
        # Convert to a percentage in convert()
        try:
            percentage = convert(user_input)
            break  # Exit loop if the input is valid
        except ValueError as e:
            print(e)  # Print error message and re-prompt
        except ZeroDivisionError:
            print("Denominator cannot be zero. Enter a new fraction: ")

    # Get fuel percentage from gauge()
    print(gauge(percentage))


def convert(fraction: str) -> int:
    # Split fraction and convert to integers
    numerator, denominator = map(int, fraction.split("/"))
    # Raise exceptions for specific cases
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if numerator > denominator:
        raise ValueError("Numerator cannot be greater than denominator")

    # Convert to a percentage -> int
    percentage = round((numerator / denominator) * 100)
    # return percentage int to main
    return percentage


def gauge(percentage: int) -> str:
    # Calculates the fuel percentage and returns a string indicating the level.fuel.py
    if percentage >= 99:
        return "F"  # Full tank
    elif percentage <= 1:
        return "E"  # Empty tank
    else:
        return f"{percentage}%"  # Normal percentage returns a str


if __name__ == "__main__":
    main()
