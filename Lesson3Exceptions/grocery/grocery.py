"""
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""

def main():
    shopping_list = {}

    while True:
        try:
            # Input an item
            item = input("")

            if shopping_list.get(item): # If the item does exist, increment the value by one
                shopping_list[item] += 1
            else:
                shopping_list[item] = 1 # If item does not exist, add the item with a value of 1
        except EOFError:
            break

    # Sort dict and capitalise keys
    sorted_list = dict(sorted(shopping_list.items()))
    capitals = {key.upper(): value for key, value in sorted_list.items()}

    for key, value in capitals.items():
        print(f"{value} {key}")

main()