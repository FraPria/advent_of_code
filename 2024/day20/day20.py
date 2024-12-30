# %% 
import numpy as np
from queue import Queue

# %% IMPORT
with open('input.txt') as f:
    mat = [list(line.rstrip()) for line in f]

mat = np.array(mat)

start_pos = np.where(mat=='S')
end_pos = np.where(mat=='E')
mat[mat=='#'] = 1
mat[mat=='.'] = 0
mat[mat=='E'] = 0
mat[mat=='S'] = 0
mat = mat.astype(float)

# %% FIND PATH
# non ho voglia di fare un algoritmo ad hoc quindi uso quello del giorno 16
# https://medium.com/@msgold/using-python-to-create-and-solve-mazes-672285723c96
def find_path(maze):
    # BFS algorithm to find the shortest path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (start_pos[0], start_pos[1])
    end = (end_pos[0], end_pos[1])
    visited = np.zeros_like(maze, dtype=bool)
    visited[start] = True
    queue = Queue()
    queue.put((start, []))
    while not queue.empty():
        (node, path) = queue.get()
        for dx, dy in directions:
            next_node = (node[0]+dx, node[1]+dy)
            if (next_node == end):
                return path + [next_node]
            if (next_node[0] >= 0 and next_node[1] >= 0 and 
                next_node[0] < maze.shape[0] and next_node[1] < maze.shape[1] and 
                maze[next_node] == 0 and not visited[next_node]):
                visited[next_node] = True
                queue.put((next_node, path + [next_node]))

path = find_path(mat)
path = [ (p[0][0], p[1][0]) for p in path ]
path = [(start_pos[0][0], start_pos[1][0])] + path # add the initial step which is returned in the find_path function

# %% PART 1
# find manhattan distance for each position in the path pairs
point_distance = []
for i in range(len(path)):
    for j in range(i+1, len(path)):
        
        d_row = abs(path[i][0]-path[j][0])
        d_col = abs(path[i][1]-path[j][1])
        if ((d_row==0) & (d_col==2)) | ((d_row==2) & (d_col==0)):
            point_distance.append(abs(j-i)-2)

# remove the pairs of points where the distance is 2 (equal to the cheat steps, so no advantange of taking them)
point_distance = sorted([ l for l in point_distance if l>0])

n = 100
len([ l for l in point_distance if l>=n])

# %% PART 2
# find manhattan distance for each position in the path pairs
point_distance = []
for i in range(len(path)):
    print(i, len(path))
    for j in range(i+1, len(path)):
        d_row = abs(path[i][0]-path[j][0])
        d_col = abs(path[i][1]-path[j][1])
        steps = d_row + d_col
        if (steps<=20):
            # If manhattan distance is less than 20 the two points are eligible for cheating
            point_distance.append(abs(j-i)-steps)

# remove the pairs of points where the distance is equal to the cheat steps (so no advantange of taking them)
point_distance = sorted([ l for l in point_distance if l>0])

# these are all right for test input
for n in [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76]: 
    l = len([ l for l in point_distance if l==n])
    print("There are "+str(l)+" cheats that save "+str(n)+" picoseconds.")


solution = len([ l for l in point_distance if l>=100])
print(solution)


# %%
