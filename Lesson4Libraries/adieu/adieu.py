import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

# A method of the inflect module, adds the commas and the "and"!
names_list = p.join(names)
print("Adieu, adieu, to " + names_list)