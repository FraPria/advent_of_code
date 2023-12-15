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
with open('day_14_test.txt') as file:
    for line in file:
        if line =='\n':
            mat = np.array(l)
            input.append(mat)
            l = []
        else:
            line = list(line.replace('\n', ''))
            l.append(line)
# %%
