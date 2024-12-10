# %%
import numpy as np

# %% Import text to numpy array matrix
with open('input.txt') as f:
    mat = [list(line.rstrip()) for line in f]

mat = np.array(mat)
mat[mat=='.']=10
mat = mat.astype(float)
mat = np.pad(mat, pad_width=1, constant_values=10)

# %% PART 1
# --> recursive tree.
def tree(m, i, j):
    print(m[i, j], i, j)
    if (m[i, j]==9):
        m[i,j] = 10 # modify the ending node, so that I don't coount it twice
        return 1  # reached the zero
    else:
        tree_right = 0
        tree_left = 0
        tree_top = 0
        tree_bottom = 0
        if m[i, j+1]== m[i,j]+1:
            tree_right = tree(m, i, j+1) 
        if m[i, j-1]== m[i,j]+1:
            tree_left = tree(m, i, j-1) 
        if m[i+1, j]== m[i,j]+1:
            tree_bottom = tree(m, i+1, j) 
        if m[i-1, j]== m[i,j]+1:
            tree_top = tree(m, i-1, j) 
        
            
    return tree_right + tree_left + tree_bottom + tree_top

# tree(mat, 7, 1)

check_nine = []
y, x = np.where(mat==0)
for k in range(len(x)):
    check_nine.append(tree(mat.copy(), y[k], x[k]))

print(sum(check_nine))



# %%
# %% PART 2
# --> recursive tree.
def tree(m, i, j):
    if (m[i, j]==9):
        # m[i,j] = 10 # PART2: JUST REMOVE THIS ROW SO THAT I COUNT ALL THE TRAILS
        return 1  # reached the zero
    else:
        tree_right = 0
        tree_left = 0
        tree_top = 0
        tree_bottom = 0
        if m[i, j+1]== m[i,j]+1:
            tree_right = tree(m, i, j+1) 
        if m[i, j-1]== m[i,j]+1:
            tree_left = tree(m, i, j-1) 
        if m[i+1, j]== m[i,j]+1:
            tree_bottom = tree(m, i+1, j) 
        if m[i-1, j]== m[i,j]+1:
            tree_top = tree(m, i-1, j) 
        
            
    return tree_right + tree_left + tree_bottom + tree_top


check_nine = []
y, x = np.where(mat==0)
for k in range(len(x)):
    check_nine.append(tree(mat.copy(), y[k], x[k]))

print(sum(check_nine))
# %%
