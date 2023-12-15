# %%
import re
import numpy as np
import os
import time
import matplotlib.pyplot as plt


# %%
def roll_north(mat):
    tilted = np.copy(mat)
    L = mat.shape[0]

    for c in range(mat.shape[1]): # run through columns
        blocks_coord = np.where(mat[:,c]=='#')[0]
        stones_coord = np.where(mat[:,c]=='O')[0]
        for i in range(len(blocks_coord)):
            if i != len(blocks_coord)-1: # not last row
                idx = (stones_coord>blocks_coord[i]) & (stones_coord<blocks_coord[i+1]) # stone falls in between two blocks
            else: # last row
                idx = stones_coord>blocks_coord[i]  # stone falls below the lowest block

            # move the stones by starting from the block_coord + 1 and incrementing by 1.
            new_rows_coord = list(range(blocks_coord[i]+1, blocks_coord[i]+1+len(stones_coord[idx]) ))

            tilted[stones_coord[idx], c] = '.' # remove old position of stones
            tilted[new_rows_coord, c] = 'O' # add stones in the new positions
    return tilted


def make_a_cycle(bordered):
    mat1 = roll_north(bordered)
    mat2 = roll_north(np.rot90(mat1, 3))
    mat3 = roll_north(np.rot90(mat2, 3))
    mat4 = roll_north(np.rot90(mat3, 3))
    return np.rot90(mat4, 3)

# ==================================
# %% Import 
l = []

# with open('day_14_test.txt') as file:
with open('day_14_input.txt') as file:
    i = 0
    for line in file:
        line = list(line.replace('\n', ''))
        if i == 0:
            l.append(['#']*len(line))    # ad top line full of "#"
            l.append(line)
        else:
            l.append(line)
        i += 1
        
mat = np.array(l)

# %% Part 1
tilted = np.copy(mat)
L = mat.shape[0]

new_mat = roll_north(mat)
load =  sum(L - np.where(new_mat=='O')[0])

print('Solution part 1 ' + str(load))   

# ==================================
# %% Part 2 (Incomplete)
bordered = np.copy(mat)
bordered = np.hstack((bordered, np.array(['#']*bordered.shape[0]).reshape(bordered.shape[0],-1))) # add "#" at the right
bordered = np.vstack((bordered, np.array(['#']*bordered.shape[1]).reshape(-1,bordered.shape[1]))) # add "#" at the bottom
bordered = np.hstack((np.array(['#']*bordered.shape[0]).reshape(bordered.shape[0],-1), bordered)) # add "#" at the left


# %%
# NOT EFFICIENT! 15 sec for 10000 --> 416 hours to make 1 billion
# but there is a pattern
start_time = time.time()
L = bordered.shape[0]
iterations = 500
load = []
for i in range(iterations):
    bordered = make_a_cycle(bordered)
    load.append( sum(L - np.where(bordered=='O')[0]-1))

end_time = time.time()
print(load)
print(end_time - start_time)

# %%
plt.figure()
plt.plot(load,'-*')
# plt.xlim(0,500)

# %% Cycle detection
prev_idx = dict()
for i in range(len(load[0:300])):
    if load[i] in load[0:(i)]:
        prev_idx.update({load[i] :  np.where(load[0:(i)]==load[i] )[0][0]})
        # prev_idx.append(np.where(load[0:(i)]==load[i] )[0][0])
        # print(str(i) +' repeats ' + str(prev_idx[-1]))

a = list(prev_idx.values())
np.array(a[1:]) - np.array(a[:-1])


# %%
