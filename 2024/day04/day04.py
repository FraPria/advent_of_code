# %%
import numpy as np
import re 

# %% Import text to numpy array matrix
with open('input.txt') as f:
    mat = [list(line.rstrip()) for line in f]

mat = np.array(mat)

# %%

#  rows
rows_count = 0
for line in mat:
    row = ''.join(map(str, line))
    rows_count = rows_count + len(re.findall('XMAS', row)) + len(re.findall('SAMX', row) )

#  cols
cols_count = 0
for line in mat.T:
    col = ''.join(map(str, line))
    cols_count = cols_count + len(re.findall('XMAS', col)) + len(re.findall('SAMX', col) )

# right diagonals
ncol = np.shape(mat)[1]

diag_right_counts = 0
for i in range(-(ncol-4), (ncol-4)):
    x = np.diagonal(mat, offset=i)
    diag_right_counts = diag_right_counts + len(re.findall('XMAS', ''.join(x))) + len(re.findall('SAMX', ''.join(x)) )

mirror_mat = np.fliplr(mat)
diag_left_counts = 0
for i in range(-(ncol-4), (ncol-4)):
    x = np.diagonal(mirror_mat, offset=i)
    diag_left_counts = diag_left_counts + len(re.findall('XMAS', ''.join(x))) + len(re.findall('SAMX', ''.join(x)) )



# 2561 too high
print('SOLUTION 1: ' + str(rows_count+cols_count+diag_right_counts+diag_left_counts))
# 2545 dovrebbe essere

# %% PART 2
c = 0
for row in range(1, np.shape(mat)[0]-1):
    for col in range(1, np.shape(mat)[1]-1):
        if (mat[row,col]=='A'):
            if (mat[row-1, col-1]=='M') & (mat[row+1, col+1]=='S') & (mat[row-1, col+1]=='M') & (mat[row+1, col-1]=='S'):
                c = c + 1
            elif (mat[row-1, col-1]=='M') & (mat[row+1, col+1]=='S') & (mat[row-1, col+1]=='S') & (mat[row+1, col-1]=='M'):
                c = c + 1
            elif (mat[row-1, col-1]=='S') & (mat[row+1, col+1]=='M') & (mat[row-1, col+1]=='S') & (mat[row+1, col-1]=='M'):
                c = c + 1
            elif (mat[row-1, col-1]=='S') & (mat[row+1, col+1]=='M') & (mat[row-1, col+1]=='M') & (mat[row+1, col-1]=='S'):
                c = c + 1
print(c)
# %%
