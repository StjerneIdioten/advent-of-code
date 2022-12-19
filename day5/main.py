import sys
import os
import re
import copy

if __name__ == "__main__":
    stacks_9000 = [[]]
    with open(os.path.join(sys.path[0], "data")) as file:
        # Create initial stacks for 9000
        while (line := file.readline()):
            if line == '\n':
                break
            stack_counter = 0
            for idx,c in enumerate(line):
                if not (idx - 1) % 4:
                    if len(stacks_9000) < (stack_counter + 1):
                            stacks_9000.append([]) 
                    if c.isalpha():
                        stacks_9000[stack_counter].append(c)
                    stack_counter += 1
        
        for stack in stacks_9000:
            stack.reverse()
        
        # Create initial stacks for 9001
        stacks_9001 = copy.deepcopy(stacks_9000)

        # Perform stack move operations
        while (line := file.readline()):
            step = re.findall(r'\d+', line)

            stacks_9000[int(step[2])-1] += stacks_9000[int(step[1])-1][-1:-int(step[0])-1:-1]
            del stacks_9000[int(step[1])-1][-int(step[0]):]

            stacks_9001[int(step[2])-1] += stacks_9001[int(step[1])-1][-int(step[0]):]
            del stacks_9001[int(step[1])-1][-int(step[0]):]
    
    print("Stack 9000:")
    top_of_stack_9000 = ""
    for stack in stacks_9000:
        print(stack)
        top_of_stack_9000 += stack[-1]
    print(f"Top of Stack: {top_of_stack_9000}")

    print("\nStack 9001:")
    top_of_stack_9001 = ""
    for stack in stacks_9001:
        print(stack)
        top_of_stack_9001 += stack[-1]
    print(f"Top of Stack: {top_of_stack_9001}")
            