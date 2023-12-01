import sys
import os

if __name__ == "__main__":
    top_three = [0, 0, 0]
    with open(os.path.join(sys.path[0], "data")) as file:
        current = 0
        while (line := file.readline()):
            if (line != '\n'):
                current += int(line)
            else:
                for idx in range(3):
                    if (current > top_three[idx]):
                        top_three.insert(idx, current)
                        top_three.pop(3)
                        break
                current = 0
    print(f"Top 3: {top_three}\nSum:{sum(top_three)}")
 