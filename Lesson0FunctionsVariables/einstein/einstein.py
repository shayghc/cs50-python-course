# An exercise using the pow() function to calculate the energy of a mass in joules

c = 300000000

print("Enter a value for mass in kg: ", end="")
mass = int(input())
# A longer explanatory output of print(f"A mass of {mass}kg represents an energy of {mass*pow(c, 2)} joules is not possible because of how the tests have been set up)
print(mass*pow(c, 2))