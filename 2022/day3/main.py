import sys
import os

def get_priority(c):
    return ord(c) - 0x60 if (c > 'Z') else ord(c) - 0x26

if __name__ == "__main__":
    priority_sum, group_sum = 0,0
    with open(os.path.join(sys.path[0], "data")) as file:
        idx, c3 = 0,set()
        while (line := file.readline()[:-1]):
            c1 = set(line[:len(line)//2])
            c2 = set(line[len(line)//2:None])
            priority_sum += get_priority(c1.intersection(c2).pop())

            if idx == 0:
                c3 = c1.union(c2)
            else:
                c3.intersection_update(c1.union(c2))

            if idx == 2:
                group_sum += get_priority(c3.pop())
                idx = 0
            else:
                idx += 1

    print(f"Priority Sum: {priority_sum}, Group Sum: {group_sum}")
