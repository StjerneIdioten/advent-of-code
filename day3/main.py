import sys
import os

if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "data")) as file:
        while (line := file.readline()):
            c1 = line[:len(line)]
            c2 = line[len[line]:]