"""
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

def main():
    # Use the get_input function to return the fuel percentage
    print(get_input())


# get_input checks for exceptions and calls calc_percentage to define levels.
def get_input():
    while True:
        try:
            x, y = input("Enter fraction of fuel: ").strip().split("/")
            x = int(x)
            y = int(y)
            percent = calc_percentage(round(x / y * 100))
        except ValueError:
            print("Value Error!")
        except ZeroDivisionError:
            print("Zero division error!")
        else:
            if x <= y:  # Checks that the user has not input a value greater than 100%
                return percent


# calc_percentafe checks for the correct level indication
def calc_percentage(level):
    if level >= 99:
        return "F"
    elif level <= 1:
        return "E"
    else:
        return str(level) + "%"

main()