"""Implement a program that:
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message."""


import sys
import csv


# scourgify.py to alter the sequence of strings in a .csv file
def main():
    new_format = []
    # Validate CLI input string
    if check_arguments_length(sys.argv):
        try:
            with open(sys.argv[1]) as before, open(sys.argv[2], "w") as after:
                reader = csv.DictReader(
                    before, fieldnames=["name", "house"], delimiter=","
                )
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                # This line writes the header row to the CSV file, based on the field names provided earlier
                writer.writeheader()
                for row in reader:
                    if row == {"house": "house", "name": "name"}:
                        continue
                    last, first = row["name"].split(",")
                    new_format = {
                        "first": first.lstrip(),
                        "last": last,
                        "house": row["house"],
                    }
                    # This line writes the content of the new_format dictionary as a row in the after CSV file
                    writer.writerow(new_format)

        except FileNotFoundError:
            sys.exit("File does not exist")
        except Exception as e:
            print(f"An error of type {type(e)} occurred: {e}")


# Check that sys.argv is the right length
def check_arguments_length(args):
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(".csv") or not args[2].endswith(".csv"):
        sys.exit("Not .csv files")
    else:
        return True


if __name__ == "__main__":
    main()
