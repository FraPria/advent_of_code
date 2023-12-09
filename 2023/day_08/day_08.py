# %%
import re
import numpy as np
import os


# %%
l = 0
positions = []
left = []
right = []
# with open('day_08_test3.txt') as file:
with open('day_08_input.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        if l==0:
            instructions=list(line)
        elif l==1:
            next
        else:
            positions.append(list(re.split(r'\ \=\ ', line))[0])
            left.append(list(re.split(r'\ \=\ |\(|\)|\,\ ', line))[2])
            right.append(list(re.split(r'\ \=\ |\(|\)|\,\ ', line))[3])
        l = l + 1

# %%
positions = np.array(positions)
left = np.array(left)
right = np.array(right)
instructions = np.array(instructions)


# ======================================
# %% Part 1
start = np.where(positions=='AAA')
end = np.where(positions=='ZZZ')
# end = [i for i in range(len(positions)) if positions[i] =='ZZZ' ]

# %% 
pos = start
steps = 0
pointer = 0
while pos != end:
    if pointer>=len(instructions):
        pointer = 0 
    
    if instructions[pointer] == 'L':
        pos = np.where(positions == left[pos])
    elif instructions[pointer] == 'R':
        pos = np.where(positions == right[pos])
    steps += 1
    pointer += 1

# ======================================
# %% Part 2
starts = [i for i in range(len(positions)) if str(positions[i]).endswith('A')]
ends = [i for i in range(len(positions)) if str(positions[i]).endswith('Z')]

# %%
all_steps = []

for s in starts:
    print(s)
    pos = s
    steps = 0
    pointer = 0
    while pos not in ends:
        if pointer>=len(instructions):
            pointer = 0 
        
        if instructions[pointer] == 'L':
            pos = np.where(positions == left[pos])[0][0]
        elif instructions[pointer] == 'R':
            pos = np.where(positions == right[pos])[0][0]
        steps += 1
        pointer += 1
    all_steps.append(steps)



# %%
from math import gcd
lcm = 1
for i in all_steps:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)



# %%
# while len(set(pos).intersection(set(set(ends))))!=len(set(pos)):
#     print(steps)
#     if pointer>=len(instructions):
#         pointer = 0 
    
#     if instructions[pointer] == 'L':

#         pos = [np.where(positions==p)[0][0] for p in left[pos]]
#     elif instructions[pointer] == 'R':
#         pos = [np.where(positions==p)[0][0] for p in right[pos]]
#     steps += 1
#     pointer += 1


# %%
