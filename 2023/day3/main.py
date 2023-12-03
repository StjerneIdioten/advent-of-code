from pathlib import Path
import math

lines = []
with open(Path(__file__).parent / "data") as file:
    while (line := file.readline().rstrip('\n\r')):
        lines.append("." + line + ".")

padding = '.' * len(lines[0])
lines = [padding] + lines + [padding]
part_number_sum = 0
gear_number_sum = 0

def extract_part_number(line, start, dir='L') -> int:
    part_number = ""
    if (dir == 'L'):
        r = list(range(0, -3, -1))
    else:
        r = list(range(0, 3, 1))

    for i in r:
        n = line[start+i]
        if n.isdigit():
            part_number += line[start+i]
        else:
            break

    if (dir == 'L'):
        return int(part_number[::-1])
    else:
        return int(part_number)
    

for i,line in enumerate(lines[1:-1], start=1):
    for j,c in enumerate(line[1:-1], start=1):
        if c != '.' and not c.isdigit():
            print(f"({i+1},{j+1}): {c}")
            part_numbers = []
            for k in range(-1, 2):
                l = lines[i+k]
                match list(map(lambda x: x.isdigit(),l[j-1:j+2])):
                    case (True, False, False):
                        part_numbers.append(extract_part_number(l, j-1))
              
                    case (True, True, False):
                        part_numbers.append(extract_part_number(l, j))

                    case (True, True, True):
                        part_numbers.append(int(l[j-1:j+2]))

                    case (True, False, True):
                        part_numbers.append(extract_part_number(l, j-1))
                        part_numbers.append(extract_part_number(l, j+1, dir='R'))

                    case (False, False, True):
                        part_numbers.append(extract_part_number(l, j+1, dir='R'))

                    case (False, True, True):
                        part_numbers.append(extract_part_number(l, j, dir='R'))

                    case (False, True, False):
                        part_numbers.append(int(l[j]))

            if part_numbers:
                part_number_sum += sum(part_numbers)
                print(f"\t{part_numbers}")
                if len(part_numbers) == 2:
                    gear_number_sum += math.prod(part_numbers)

print(f"Part Number Sum: {part_number_sum}")
print(f"Gear Number Sum: {gear_number_sum}")
            
        