# %%
import numpy as np

# %% Import text to numpy array matrix
with open('input.txt') as f:
    mat = [list(line.rstrip()) for line in f]

mat = np.array(mat)


# %% PART 1
antinodes = np.zeros(np.shape(mat))

antennas = np.unique(mat)
antennas = antennas[antennas!='.']

for a in antennas:
    y, x = np.where(mat==a)
    coords = np.array(list(zip(y, x)))

    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            print(i,j)
            d = coords[i]-coords[j]
            # project the points to the opposite side
            anti1 = coords[i] + d
            anti2 = coords[j] - d
            print(anti1, anti2)
            if (anti1[0]>=0) & (anti1[0] < np.shape(mat)[0]) & (anti1[1]>=0) & (anti1[1] < np.shape(mat)[1]):
                antinodes[anti1[0], anti1[1]] = 1

            if (anti2[0]>=0) & (anti2[0] < np.shape(mat)[0]) & (anti2[1]>=0) & (anti2[1] < np.shape(mat)[1]):
                antinodes[anti2[0], anti2[1]] = 1

print(sum(sum(antinodes)))     

# %% PART 2
antinodes = np.zeros(np.shape(mat))

antennas = np.unique(mat)
antennas = antennas[antennas!='.']

for a in antennas:
    y, x = np.where(mat==a)
    coords = np.array(list(zip(y, x)))

    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            print(i,j)
            d = coords[i]-coords[j]
            # add this to consider all the distance multipliers
            for m in range(np.shape(mat)[0]):
                anti1 = coords[i] + d*m
                anti2 = coords[j] - d*m
                print(anti1, anti2)
                if (anti1[0]>=0) & (anti1[0] < np.shape(mat)[0]) & (anti1[1]>=0) & (anti1[1] < np.shape(mat)[1]):
                    antinodes[anti1[0], anti1[1]] = 1

                if (anti2[0]>=0) & (anti2[0] < np.shape(mat)[0]) & (anti2[1]>=0) & (anti2[1] < np.shape(mat)[1]):
                    antinodes[anti2[0], anti2[1]] = 1

print(sum(sum(antinodes)))    
# %%
