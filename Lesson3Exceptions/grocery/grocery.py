"""
In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""

def main():
    """Main function to create a grocery list from user input."""
    shopping_list = {}

    while True:
        try:
            item = input("").strip()  # Read input and remove any leading/trailing whitespace
            
            # Treat input case-insensitively
            item_upper = item.upper()  

            # Increment item count in the shopping list
            if item_upper in shopping_list:
                shopping_list[item_upper] += 1
            else:
                shopping_list[item_upper] = 1
        except EOFError:
            break

    # Sort items and prepare to display the list
    sorted_list = sorted(shopping_list.items())

    for item, count in sorted_list:
        print(f"{count} {item}")  # Print count and item

if __name__ == "__main__":
    main()
