import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if clock := re.search(r"(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (AM|PM)", s):
        start_h = int(clock.group(1))
        start_m = clock.group(2)
        start_time = clock.group(3)
        end_h = int(clock.group(4))
        end_m = clock.group(5)
        end_time = clock.group(6)

        if start_m == None:
            start_m = 00
        if end_m == None:
            end_m = 00

        if (
            0 <= start_h <= 12
            and 0 <= end_h <= 12
            and 0 <= int(start_m) < 60
            and 0 <= int(end_m) < 60
        ):
            if start_h == 12 and start_time == "AM":
                start_h = 00
            if end_h == 12 and start_time == "AM":
                end_h = 00

            if start_time == "PM" and start_h < 12:
                start_h = int(start_h) + 12
            if end_time == "PM" and end_h < 12:
                end_h = int(end_h) + 12

            return f"{start_h:02d}:{int(start_m):02d} to {end_h:02d}:{int(end_m):02d}"


    raise ValueError


if __name__ == "__main__":
    main()
