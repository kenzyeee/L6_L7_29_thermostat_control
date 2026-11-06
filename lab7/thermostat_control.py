import math
import re


_SETPOINT = re.compile(r"^\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*([cCfF])\s*$")


def parse_setpoint(text):
    if not isinstance(text, str):
        raise TypeError("setpoint must be text")
    match = _SETPOINT.fullmatch(text)
    if match is None:
        raise ValueError("setpoint must be a number followed by C or F")
    value = float(match.group(1))
    if not math.isfinite(value):
        raise ValueError("setpoint must be finite")
    if match.group(2).upper() == "F":
        value = (value - 32) * 5 / 9
    return round(value, 1)


def average_temperature(readings_csv):
    if not isinstance(readings_csv, str):
        raise TypeError("readings must be comma-separated text")
    parts = readings_csv.split(",")
    if not parts or any(not part.strip() for part in parts):
        raise ValueError("readings must contain one or more numbers")
    try:
        values = [float(part.strip()) for part in parts]
    except ValueError as exc:
        raise ValueError("readings must contain only numbers") from exc
    if any(not math.isfinite(value) for value in values):
        raise ValueError("readings must be finite numbers")
    return sum(values) / len(values)


def schedule_slot(time_text):
    if not isinstance(time_text, str):
        raise TypeError("time must be text in HH:MM format")
    match = re.fullmatch(r"\s*(\d{1,2}):(\d{1,2})\s*", time_text)
    if match is None:
        raise ValueError("time must be in HH:MM format")
    hour, minute = (int(part) for part in match.groups())
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError("time must be a valid 24-hour time")
    if hour < 6:
        return f"night {minute:02d}"
    return f"day {minute}"


def main():
    print("==== Running parse_setpoint ====")
    user_input = input("Enter a setpoint (e.g. 21.5C or 70F): ")
    result = parse_setpoint(user_input)
    print("Setpoint in Celsius:", result)

    print("\n==== Running average_temperature ====")
    user_input = input("Enter sensor readings as CSV (e.g. 20.5,21,22.5): ")
    result = average_temperature(user_input)
    print("Average Temperature:", result)

    print("\n==== Running schedule_slot ====")
    user_input = input("Enter a time as HH:MM (e.g. 07:30): ")
    result = schedule_slot(user_input)
    print("Schedule Slot:", result)


if __name__ == "__main__":
    main()
