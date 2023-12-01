from pathlib import Path
from itertools import islice
import re

if __name__ == "__main__":
    with open(Path(__file__).parent / "data") as file:
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        spellings = ["one", "two", "six", "nine", "four", "five", "three", "seven", "eight"]

        calibration_value_digits = 0
        while (line := file.readline().rstrip('\n\r')):
            last_idx = len(line) - 1
            earlist_digit_idx = last_idx
            latest_digit_idx = 0
            #print(f"'{line}'")
            for digit in digits:
                if (earlist_digit_idx != 0) and ((idx := line.find(digit, 0, earlist_digit_idx)) != -1) and (idx < earlist_digit_idx):
                    if (earlist_digit_idx := idx) == 0 and latest_digit_idx == last_idx:
                        break

                if (latest_digit_idx != last_idx) and ((idx := line.rfind(digit, latest_digit_idx, last_idx + 1)) != -1) and (idx > latest_digit_idx):
                    if (latest_digit_idx := idx) == last_idx and earlist_digit_idx == 0:
                        break          
            calibration_value_digits += int(f"{line[earlist_digit_idx]}{line[latest_digit_idx]}")         
        print(calibration_value_digits)