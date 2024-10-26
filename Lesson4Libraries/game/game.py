import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except TypeError:
        continue
    except ValueError:
        continue

random_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0 and guess <= level:
            if guess > random_number:
                print("Too large!")
            elif guess < random_number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass