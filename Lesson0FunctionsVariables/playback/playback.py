# Another exercise using the replace() str method using emojis
# This code employs the main() function to call the convert() function

cd/def main():
    convert(input("How are you feeling today? "))

def convert(mood):
    print(mood.replace(":)", "🙂").replace(":(", "🙁"))

main()