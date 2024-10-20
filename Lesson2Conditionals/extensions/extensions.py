"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

# Uses if, elif, else statements to determine the media type of the file based on its suffix.
def main():
    name = input("File name: ").strip().lower()

    if name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".jpg"):
        print("image/jpeg")
    elif name.endswith(".jpeg"):
        print("image/jpeg")
    elif name.endswith(".png"):
        print("image/png")
    elif name.endswith(".pdf"):
        print("application/pdf")
    elif name.endswith(".txt"):
        print("text/plain")
    elif name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
# Alternative solution using match for extension mapping:
"""
def main():
    unpacked = input("File name: ").strip().lower().split(".")
    extension = unpacked[len(unpacked)-1]

    match extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
"""
