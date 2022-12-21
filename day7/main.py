import sys
import os
import bisect

def pprint(str, indent):
    print(f"{'  '*indent}{str}")

dir_sizes = []

if __name__ == "__main__":
    with open(os.path.join(sys.path[0], "data")) as file:
        file.readline()
        def interpret(indent = 0):
            size = 0
            while line := file.readline()[:-1]:
                if line[0] == '$':
                    cmd = line[2:4]
                    if cmd == "cd":
                        if line[5:7] == "..": # cd out of folder
                            return size
                        else: # cd into folder
                            pprint(f"⤵ {line[5:]}", indent)
                            dir_size = interpret(indent+1)
                            bisect.insort(dir_sizes, dir_size)
                            size += dir_size
                            pprint(f"⬆ {dir_size} {line[5:]}", indent)
                    else: # ls
                        pprint("🔍", indent)
                else: # Folder or file listing
                    if line[0:3] == "dir":
                        pprint(f"📁 {line[4:]}", indent)
                    else:
                        pprint(f"📄 {line}", indent)
                        size += int(line[0:line.find(' ')])
            return size
        dir_sizes.append(interpret())

        print(f"Total Size: {dir_sizes[-1]}")

        less_than_100000 = 0
        for dir_size in dir_sizes:
            if dir_size <= 100000:
                less_than_100000 += dir_size
                break
        for dir_size in dir_sizes:
            if dir_size >= (30000000 - (70000000 - dir_sizes[-1])):
                print(f"Smallest dir: {dir_size}")
                break

        print(f"Less than 10000: {less_than_100000}")
            

            