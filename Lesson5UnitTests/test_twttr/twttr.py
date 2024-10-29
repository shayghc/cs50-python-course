def main():
    print(shorten(input("Input: ")))


# shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether input in uppercase or lowercase.
def shorten(word):
    vowels = "AEIOUaeiou"
    altered_string = ""

    for char in word:
        if char not in vowels:
            altered_string += char

    return altered_string


if __name__ == "__main__":
    main()
