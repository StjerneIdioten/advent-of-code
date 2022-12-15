import sys
import os

if __name__ == "__main__":
    priority_sum = 0
    with open(os.path.join(sys.path[0], "data")) as file:
        while (line := file.readline()[:-1]):
            c = set(line[:len(line)//2]).intersection(set(line[len(line)//2:None])).pop()
            priority_sum += ord(c) - 0x60 if (c > 'Z') else ord(c) - 0x26
    print(f"{priority_sum}")
