# %%

import re
import numpy as np
import os

# %%
input = []
with open('day_10_test.txt') as file:
    for line in file:
        line = list(line.replace('\n', ''))
        input.append(line)

x = np.array(input)

# %%
h = np.shape(x)[0]
w = np.shape(x)[1]
mat = np.array(['.']*(w+2)*(h+2)).reshape(w+2,h+2)
mat[1:-1,1:-1] = x


# %%
# find S
S = np.where(mat=='S')

move = []
if (mat[S[0]+1, S[1]] == '|') | (mat[S[0]+1, S[1]] == 'L') | (mat[S[0]+1, S[1]] == 'J'): 
    # check down
    move.append('down')
    vertical = 1
    horizontal = 0
elif (mat[S[0]-1, S[1]] =='|') | (mat[S[0]-1, S[1]] =='F') | (mat[S[0]-1, S[1]] =='7'):
    # check up
    move.append('up')
    vertical = -1
    horizontal = 0
elif (mat[S[0], S[1]+1]=='-') | (mat[S[0], S[1]+1] =='J') | (mat[S[0], S[1]+1]=='7'):
    # check right
    move.append('right')
    vertical = 0
    horizontal = 1
elif (mat[S[0], S[1]-1]=='-') | (mat[S[0], S[1]-1]=='L') | (mat[S[0], S[1]-1]=='F'):
    # check left
    move.append('left')
    vertical = 0
    horizontal = -1


# %%
