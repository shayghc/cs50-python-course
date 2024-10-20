"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
"""
def main():
    # Separate elements
    x, y, z = input("Expression: ").split(" ")
    x = float(x)
    z = float(z)

    # Calculate result
    match y:
        case "+":
            print(round(x + z, 1))
        case "-":
            print(round(x - z, 1))
        case "/":
            print(round(x / z, 1))
        case "*":
            print(round(x * z, 1))

main()