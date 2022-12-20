import sys
import os
from collections import deque

if __name__ == "__main__":
    package_position = 0
    with open(os.path.join(sys.path[0], "data")) as file:
        window = deque()
        def readNext():
            while (c := file.read(1)):
               yield c
        for read_position,c in enumerate(readNext(), start=1):
            window.append(c)
            if (package_position == 0) and (read_position >= 4):
                if len(window) == len(set(window)):
                    package_position = read_position
                    print(f"Package Marker end: ({package_position}, {c})")
                else:
                    window.popleft()
            elif (package_position != 0) and (read_position >= package_position + 10):
                if len(window) == len(set(window)):
                    print(f"Message Marker end: ({read_position}, {c})")
                    break
                else:
                    window.popleft()
                
    