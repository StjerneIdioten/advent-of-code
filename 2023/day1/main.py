from pathlib import Path
from itertools import islice
import re

if __name__ == "__main__":
    with open(Path(__file__).parent / "data") as file:
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        spellings = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

        calibration_value_only_digits = 0
        calibration_value_both = 0

        while (line := file.readline().rstrip('\n\r')):
            first_digit = len(line)
            last_digit = 0
            for digit in digits:
                if (digit_idx := line.find(digit)) != -1:
                    if digit_idx < first_digit:
                        first_digit = digit_idx
                if (digit_idx := line.rfind(digit)) != -1:
                    if digit_idx > last_digit:
                        last_digit = digit_idx 

            calibration_value_only_digits += int(f"{line[first_digit]}{line[last_digit]}")
        
            first_digit = (first_digit, line[first_digit])
            last_digit = (last_digit, line[last_digit])
            for spelling in spellings.keys():
                if (digit_idx := line.find(spelling)) != -1:
                    if digit_idx < first_digit[0]:
                        first_digit = (digit_idx, spellings[spelling])
                if (digit_idx := line.rfind(spelling)) != -1:
                    if digit_idx > last_digit[0]:
                        last_digit = (digit_idx, spellings[spelling])

            calibration_value = int(f"{first_digit[1]}{last_digit[1]}")
            calibration_value_both += calibration_value

        print(f"Digits Only: {calibration_value_only_digits}")
        print(f"Digits And Spellings: {calibration_value_both}")