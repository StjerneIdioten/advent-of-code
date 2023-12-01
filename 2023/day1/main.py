from pathlib import Path
from itertools import islice
import re

if __name__ == "__main__":
    with open(Path(__file__).parent / "data") as file:
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        spellings = {"one": "1", "two": "2", "six": "6", "nine": "9", "four": "4", "five": "5", "three": "3", "seven": "7", "eight": "8"}

        calibration_value_only_digits = 0
        calibration_value_both = 0
        while (line := file.readline().rstrip('\n\r')):
            first_digit = ""
            last_digit = ""
            last_idx = len(line) - 1
            earliest_digit_idx = last_idx
            latest_digit_idx = 0
            for digit in digits:
                if (earliest_digit_idx != 0) and ((idx := line.find(digit, 0, earliest_digit_idx)) != -1) and (idx < earliest_digit_idx):
                    if (earliest_digit_idx := idx) == 0 and latest_digit_idx == last_idx:
                        break

                if (latest_digit_idx != last_idx) and ((idx := line.rfind(digit, latest_digit_idx, last_idx + 1)) != -1) and (idx > latest_digit_idx):
                    if (latest_digit_idx := idx) == last_idx and earliest_digit_idx == 0:
                        break  
            
            first_digit = line[earliest_digit_idx]
            last_digit = line[latest_digit_idx]

            calibration_value_only_digits += int(f"{first_digit}{last_digit}")

            earliest_spelling_idx = earliest_digit_idx
            latest_spelling_idx = latest_digit_idx

            for spelling in spellings.keys():
                lline = line[0:earliest_spelling_idx]
                if len(spelling) <= len(lline):
                    idx = lline.find(spelling, 0, earliest_spelling_idx)
                    if idx != -1: 
                        earliest_spelling_idx = idx + 1
                        first_digit = spellings[spelling]
                        if earliest_spelling_idx == 0 and latest_spelling_idx == last_idx:
                            break
            
                rline = line[latest_spelling_idx + 1: last_idx + 1]
                if len(spelling) <= len(rline):
                    idx = rline.find(spelling, 0, last_idx + 1)
                    if (idx != -1):
                        latest_spelling_idx += idx + len(spelling)
                        last_digit = spellings[spelling]
                        if latest_spelling_idx == last_idx and earliest_spelling_idx == 0:
                            break

            
            cal_val = int(f"{first_digit}{last_digit}")
            print(f"'{line}':{cal_val}")
            calibration_value_both += cal_val

        print(f"Digits Only: {calibration_value_only_digits}")
        print(f"Digits And Spellings: {calibration_value_both}")