import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        try:
            octet1 = int(matches.group(1))
            octet2 = int(matches.group(2))
            octet3 = int(matches.group(3))
            octet4 = int(matches.group(4))
            if (
                0 <= octet1 <= 255
                and 0 <= octet2 <= 255
                and 0 <= octet3 <= 255
                and 0 <= octet4 <= 255
            ):
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False


if __name__ == "__main__":
    main()