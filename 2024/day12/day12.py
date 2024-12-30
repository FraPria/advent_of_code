# %%
import numpy as np

# %% Import text to numpy array matrix
with open('input.txt') as f:
    mat = [list(line.rstrip()) for line in f]

mat = np.array(mat)
mat = mat.view(np.int32)

# %% TRANSFORM INPUT INTO UNIQUE CLUSTERS OF NUMBERS
# https://stackoverflow.com/questions/47523071/grouping-adjacent-equal-elements-of-a-2d-numpy-array
from scipy.ndimage import label
values = np.unique(mat.ravel())
offset = 0
mat2 = np.zeros_like(mat)
for v in values:
  labeled, num_features = label(mat == v)
  mat2 += labeled + offset*(labeled > 0)
  offset += num_features
print(mat2)

# %% PART 1

def group_value(m, cell):
    rows, cols = np.where(m==cell)
    nodes = len(rows)
    edges = nodes*4
    shared_border = 0
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            # euclidian distance: I don't want diagolal connection
            # I consider two squares neighbors if their distance is just 1, no more.
            d = (rows[i]-rows[j])**2 + (cols[i]-cols[j])**2
            if d==1:
                shared_border = shared_border + 2
    edges = edges-shared_border
    return nodes*edges

res = 0
for v in list(np.unique(mat2)):
    res = res + group_value(mat2.copy(), v)


print(res)