import emoji
"""
In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
"""

  
def main():
    user_code = input("Enter an emoji code: ")
    # The language parameter allows aliases to be recognised
    converted_to_emoji = emoji.emojize(user_code, language='alias')
    print("Output: ", converted_to_emoji)
    
if __name__ == "__main()__":
    main()