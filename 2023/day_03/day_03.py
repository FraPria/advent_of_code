# %% 
import os
import re
import numpy as np
import itertools
from scipy import signal


# %%
# with open('day_03_test2.txt') as file:
with open('day_03_input.txt') as file:
    txt = [line.rstrip() for line in file]

# =======================================
# %% Part 1
num_mat = -np.ones((len(txt), len(txt[0]))) # negative numbers are the non digits cells
sym_mat = np.zeros((len(txt), len(txt[0]))) 

for row in range(len(txt)):
    numbers = re.findall(r'\d+', txt[row]) 
    # first I loop for the short numbers like 79, because if there is a bigger number containing 79 (such as 798 or 179), 
    # the values in the matrix num_mat should be overwritten with the biggest number.
    numbers = sorted(numbers, key=lambda x: (len(x), x)) 

    symbols = re.findall(r'[^\d+\.]|\+', txt[row]) # symbols, escaping numbers and dots ([^ ] operator)
    idx_sym =  [list(range(m.start(0), m.end(0))) for m in re.finditer(r'[^\d+\.]|\+', txt[row])] # ranges of symbols
    idx_sym = [item for sublist in idx_sym for item in sublist]
    sym_mat[row, idx_sym]=1

    for n in numbers:
        idx = [list(range(m.start(0), m.end(0))) for m in re.finditer(n, txt[row])]
        idx_flat = [item for sublist in idx for item in sublist]
        num_mat[row, idx_flat]=n
    

# Apply a 2D convolution with a 3x3 kernel and we check which value are bigger than 0.
neighbors = (signal.convolve2d(sym_mat, np.ones((3,3)), mode='same')>0).astype(int)
hits = np.transpose(np.where((num_mat!=-1) & (neighbors)))

# %%
# remove consecutive cells
unique_hits = hits
to_remove = list()
for i in range(len(hits)-1):
    if (hits[i+1][0] == hits[i][0]) & (hits[i+1][1] == hits[i][1]+1): # if there are two consecutive numbers, I only keep it once
        to_remove.append( i+1)

unique_hits = np.delete(unique_hits, to_remove, axis=0)

# %%
# solution1 = sum(num_mat[hits[:,0], hits[:,1]])
# print(solution1)
solution1 = sum(num_mat[unique_hits[:,0], unique_hits[:,1]])
print(solution1)

# =======================================
# %% Part 2
# with open('day_03_test2.txt') as file:
with open('day_03_input.txt') as file:
    txt = [line.rstrip() for line in file]

star_mat = np.zeros((len(txt), len(txt[0]))) 

for row in range(len(txt)):
    idx_stars =  [list(range(m.start(0), m.end(0))) for m in re.finditer(r'\*', txt[row])] # position of stars
    idx_stars = [item for sublist in idx_stars for item in sublist]
    star_mat[row, idx_stars]=1

# %%
star_positions = np.transpose(np.where(star_mat!=0))
prod = []
for r in star_positions:
    grid = np.meshgrid([r[0]-1, r[0], r[0]+1], [r[1]-1, r[1], r[1]+1])
    x = grid[0].transpose().reshape(1,-1)
    y = grid[1].transpose().reshape(1,-1)
    star_neighbors = num_mat[x,y]
    contacts = np.unique(star_neighbors[star_neighbors!=-1])
    if len(contacts)==2:
        # it's a gear
        prod.append(contacts[0]*contacts[1])

solution2 = np.sum(prod)
print(solution2)

