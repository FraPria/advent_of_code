# %%
import numpy as np


# %%
lst = []
cmd = []
with open('input.txt') as f:
    for line in f:
        if '#' in line:
            lst.append(list(line.rstrip()))
        elif '^' in line:
            cmd = cmd+list(line.rstrip())


mat = np.array(lst)
upmat = mat.copy()

# %%

