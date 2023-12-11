# %%

import re
import numpy as np
import os
from math import sqrt

# %%
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))
 

# %%
input = []
# with open('day_11_test.txt') as file:
with open('day_11_input.txt') as file:
    for line in file:
        line = list(line.replace('\n', ''))
        input.append(line)

mat = np.array(input)

empty_rows = np.where((mat[None, :]=='.').all(-1) )[1] # find rows with all '.'
empty_cols = np.where((mat[:,None]=='.').all(0) )[1] # find columns with all '.'

galaxy_coord = np.transpose(np.where(mat=='#'))

#
n = (len(galaxy_coord)*(len(galaxy_coord)-1))/2
print('Number of pairs = ' + str(n))

# %%
expansion = 10
d = []
for i in range(len(galaxy_coord[:,0])):
    for j in range(i+1, len(galaxy_coord[:,0])): 
        print(i,j)
        manh_dist = manhattan(galaxy_coord[i,:], galaxy_coord[j,:] )
        expansion_y = (expansion-1)*sum(((empty_rows>galaxy_coord[i,0]) & (empty_rows<galaxy_coord[j,0])) | (empty_rows>galaxy_coord[j,0]) & (empty_rows<galaxy_coord[i,0]))
        expansion_x = (expansion-1)*sum(((empty_cols>galaxy_coord[i,1]) & (empty_cols<galaxy_coord[j,1])) | (empty_cols>galaxy_coord[j,1]) & (empty_cols<galaxy_coord[i,1]))
        d.append(manh_dist+expansion_y+expansion_x)

print(sum(d))
# %%
