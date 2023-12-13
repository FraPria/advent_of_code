# %%
import re
import numpy as np
import os
from math import sqrt

# %%
input = []
l = []
# with open('day_13_test.txt') as file:
# with open('day_13_test2.txt') as file:
with open('day_13_input.txt') as file:
    for line in file:
        if line =='\n':
            mat = np.array(l)
            input.append(mat)
            l = []
        else:
            line = list(line.replace('\n', ''))
            l.append(line)


# %%
def find_vertical_reflection(tmp, smudge=0):
        left = 0
        for j in range(0, tmp.shape[1]-1):
            l = min(j+1, tmp.shape[1]-j-1)
            reflection_point = np.sum(tmp[:,(j-l+1):(j+1)] != np.flip(tmp[:, (j+1):(j+l+1)], axis = 1)) # reflection
            if reflection_point==smudge:
                left += j+1
        return(left)

# ===============================
# %% Part 1
result = []

for i in range(len(input)):
    tmp = input[i]
    # check reflection points on columns
    left = find_vertical_reflection(tmp)
    # check reflection points on rows
    above = find_vertical_reflection(np.transpose(tmp))
    result.append(left+100*above)

print(sum(result))

# ===============================
# %% Part 2
result = []

for i in range(len(input)):
    tmp = input[i]
    # check reflection points on columns
    left = find_vertical_reflection(tmp, smudge=1)
    # check reflection points on rows
    above = find_vertical_reflection(np.transpose(tmp), smudge=1)
    result.append(left+100*above)

print(sum(result))
# %%
