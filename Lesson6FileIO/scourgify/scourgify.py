import sys
import csv


# scourgify.py to alter the sequence of strings in a .csv file
def main():
    # Validate CLI input string
    validate_arguments(sys.argv)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file) as before, open(output_file, "w", newline="") as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                try:
                    # Split the name and handle errors
                    last, first = row["name"].split(",")
                    writer.writerow(
                        {
                            "first": first.strip(),
                            "last": last.strip(),
                            "house": row["house"],
                        }
                    )
                except ValueError:
                    print(f"Skipping invalid name format: {row['name']}")

    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        print(f"An error of type {type(e)} occurred: {e}")


# Check that sys.argv is the right length
def validate_arguments(args):
    if len(args) != 3:
        sys.exit("Please provide exactly two command-line arguments")
    if not all(arg.endswith(".csv") for arg in args[1:]):
        sys.exit("Both arguments must be .csv files")


if __name__ == "__main__":
    main()