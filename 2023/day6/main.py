from pathlib import Path
from math import (sqrt, floor, prod)

def calculate_race(max_time, record_time):
    return (max_time + 1) - 2 * floor((max_time - sqrt(pow(max_time, 2) - 4 * record_time)) / 2 + 1)

with open(Path(__file__).parent / "data") as file:
    race_lines = [line.split()[1:] for line in file.readlines()]
    print(f"Many Races: {prod([calculate_race(*race) for race in zip(map(int, race_lines[0]), map(int, race_lines[1]))])}")
    print(f"Big Race: {calculate_race(*[int(''.join(line)) for line in race_lines])}")
    
