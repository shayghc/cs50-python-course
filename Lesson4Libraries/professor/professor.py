import random

def main():
    level = get_level()

    questions = 10
    count = 0
    # While loop for questions
    while questions > 0:
        questions -= 1
        # Call for two random number of level digits
        summand1 = int(generate_integer(level))
        summand2 = int(generate_integer(level))
        sum = summand1 + summand2

        # While loop for answer attempts
        attempts = 3
        while attempts > 0:
            try:
                attempts -= 1
                guess = int(input(f"{summand1} + {summand2} = "))
                if guess == sum:
                    count += 1
                    break
                elif guess != sum and attempts > 0:
                    print("EEE")
                else:
                    print(f"{summand1} + {summand2} = {sum}")
            except:
                print("EEE")
    print(f"Score: {count}")

# Prompts for a level: 1, 2 or 3
# Check for valid input here
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                continue
            else:
                return level
        except:
            pass

# Returns a randomly generated non-negative integer with 'level' digits
def generate_integer(level):
    if level == 1:
        random_integer = random.randint(0, 9)
    elif level == 2:
        random_integer = random.randint(10, 99)
    else:
        random_integer = random.randint(100, 999)

    return random_integer


if __name__ == "__main__":
    main()