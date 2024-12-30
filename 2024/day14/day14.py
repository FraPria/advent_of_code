# %%
import re
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# %%
width = 101
height = 103

def move(x, y, v_x, v_y):
    new_x = (x+v_x)%(width)
    new_y = (y+v_y)%(height)
    return new_x, new_y

mat = np.zeros((height, width))
with open('input.txt') as f:
    for line in f:
        x = int(re.split('p=|v=|, |,|\n', line)[1])
        y = int(re.split('p=|v=|, |,|\n', line)[2])
        v_x = int(re.split('p=|v=|, |,|\n', line)[3])
        v_y = int(re.split('p=|v=|, |,|\n', line)[4])

        for s in range(100):
            x, y = move(x, y, v_x,v_y)

        mat[y,x]=mat[y,x]+1
        
print(mat)


q1 = mat[0:int(((height-1)/2)), 0:int(((width-1)/2))]
q2 = mat[0:int(((height-1)/2)), int((width-1)/2 +1):width]
q3 = mat[int((height-1)/2 +1):height, 0:int(((width-1)/2))]
q4 = mat[int((height-1)/2 +1):height, int((width-1)/2 +1):width]


print(sum(sum(q1)) * sum(sum(q2)) * sum(sum(q3))  * sum(sum(q4)))


# %% PART 2
x = []
y = []
v_x = []
v_y = []

mat = np.zeros((height, width))
with open('input.txt') as f:
    for line in f:
        x.append(int(re.split('p=|v=|, |,|\n', line)[1]))
        y.append(int(re.split('p=|v=|, |,|\n', line)[2]))
        v_x.append(int(re.split('p=|v=|, |,|\n', line)[3]))
        v_y.append(int(re.split('p=|v=|, |,|\n', line)[4]))

# I found a pattern repeated every 103 steps starting from 93
# for s in range(2000):
#     mat = np.zeros((height, width))
#     for i in range(len(x)):
#         x[i], y[i] = move(x[i], y[i], v_x[i], v_y[i])
#         mat[y,x]=mat[y,x]+1
#     Image.fromarray(mat).save("figures/"+str(f'{s:03}')+".tiff")

# save only steps the are 93+103*s --> 6377 is a christmas tree
# for s in range(10000):
#     mat = np.zeros((height, width))
#     for i in range(len(x)):
#         x[i], y[i] = move(x[i], y[i], v_x[i], v_y[i])
#         mat[y,x]=mat[y,x]+1
#     if (s-93) % 103 == 0:
#         Image.fromarray(mat).save("figures2/"+str(f'{s:03}')+".tiff")

# %%

def move_ntimes(x, y, v_x, v_y, time):
    new_x = (x+v_x*time)%(width)
    new_y = (y+v_y*time)%(height)
    return new_x, new_y


for i in range(len(x)):
    mat = np.zeros((height, width))
    x[i], y[i] = move_ntimes(x[i], y[i], v_x[i], v_y[i], 6377)
    mat[y,x]=mat[y,x]+1

Image.fromarray(mat).save("a.tiff")


# %%
