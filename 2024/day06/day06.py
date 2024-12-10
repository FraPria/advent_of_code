# %%
import numpy as np
import re 

# %% Import text to numpy array matrix
with open('input.txt') as f:
    mat = [list(line.rstrip()) for line in f]

mat = np.array(mat)
pos = np.where(mat=='^')

# %% PART 1
nrot = 0
while pos[0][0]!=0:
    nrow = np.shape(mat)[0]
    ncol = np.shape(mat)[1]
    pos = pos[0]-1, pos[1]
    print(pos)
    print(mat)
    if mat[pos]=='#':
        # rotate the matrix
        mat = np.rot90(mat)
        pos = ncol-pos[1]-1, pos[0]+1
        nrot = nrot +1
    else:
        mat[pos] ='X'
        
# 4579 too low
print(len(np.where(mat=='X')[0]))

# %%