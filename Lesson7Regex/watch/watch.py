import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str or None:
    """
    Parse an HTML string to extract the YouTube video ID from an iframe source URL.

    Parameters:
    s (str): The HTML string to parse.

    Returns:
    str: The YouTube video ID if found, otherwise None.
    """
    if matches := re.search(r"(?:<iframe src=\")https?:\/\/(?:www\.)?youtube\.com\/(?:embed\/)?(\w+)", s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()