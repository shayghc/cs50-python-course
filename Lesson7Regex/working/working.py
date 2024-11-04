import re


def main():
    print(convert(input("Hours: ")))


def convert(time: str) -> str:
    """
    Converts a time from 12-hour format to 24-hour format.

    Parameters:
    time (str): A string representing the time in 12-hour format. The time should be in one of the following formats:
        - "HH:MM AM to HH:MM PM"
        - "H:MM AM to H:MM PM"
        - "HH:MM AM to H:MM PM"
        - "H:MM AM to HH:MM PM"

    Returns:
    str: A string representing the time in 24-hour format. The format is "HH:MM to HH:MM".
        If the input time is invalid (e.g., minute > 59, hour > 12), a ValueError is raised.

    Raises:
    ValueError: If the input time is not in a permitted format or if either time is invalid.
    """
    try:
        if matches := re.search(
            r"^([1]?[0-9]):?([0-5][0-9])? (AM|PM) to ([1]?[0-9]):?([0-5][0-9])? (AM|PM)$",
            time,
        ):
            times = matches.groups()
            times_list = list(times)
            if int(times_list[0]) > 12 or int(times_list[3]) > 12:
                raise ValueError
            return convert_to_24hr(times_list)
        else:
            raise ValueError
    except ValueError:
        raise ValueError


def convert_to_24hr(time):
    """
    Converts a time from 12-hour format to 24-hour format.

    Parameters:
        time (List[str]): A list containing the time in 12-hour format. The list should have the following structure:
        [start_hour, start_minute, start_meridien, end_hour, end_minute, end_meridien]
        start_hour, end_hour: Strings representing the hour in 12-hour format.
        start_minute, end_minute: Strings representing the minute in 12-hour format.
        start_meridien, end_meridien: Strings representing the meridien (AM or PM) in 12-hour format.

    Returns:
        str: A string representing the time in 24-hour format. The format is "HH:MM to HH:MM".
        If the input time is invalid (e.g., minute > 59), a ValueError is raised.
    """
    start_hour, start_minute = handle_meridien(time[0], time[1], time[2])
    end_hour, end_minute = handle_meridien(time[3], time[4], time[5])

    if int(start_minute) > 59 or int(end_minute) > 59:
        raise ValueError
    else:
        return f"{int(start_hour):02}:{int(start_minute):02} to {int(end_hour):02}:{int(end_minute):02}"


def handle_meridien(hour, minute, meridien):
    """
    This function handles the conversion of 12-hour format to 24-hour format for a given hour, minute, and meridien.

    Parameters:
    hour (str): A string representing the hour in 12-hour format.
    minute (str): A string representing the minute in 12-hour format.
    meridien (str): A string representing the meridien (AM or PM) in 12-hour format.

    Returns:
    Tuple[str, str]: A tuple containing the converted hour and minute in 24-hour format.
    """
    if meridien == "AM" and int(hour) == 12:
        hour = "00"
    if meridien == "PM" and int(hour) != 12:
        new_hour = int(hour) + 12
        hour = str(new_hour)
    if minute == None:
        minute = "00"

    return hour, minute


if __name__ == "__main__":
    main()
