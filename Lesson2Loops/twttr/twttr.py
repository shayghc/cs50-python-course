"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

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
