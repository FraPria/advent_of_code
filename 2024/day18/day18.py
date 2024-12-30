# %% 
import numpy as np
from queue import Queue

# %% PART 1
size=71
bytes = 1024

mat = np.zeros((size, size))

c=0
with open('input.txt') as f:
    for line in f:
        col, row = line.rstrip().split(',')
        col = int(col)
        row = int(row)
        if c<bytes:
            mat[row, col] = 1
        c=c+1

mat

pos =(0,0)
end_pos=(size-1,size-1)

# %% PART 1
# https://medium.com/@msgold/using-python-to-create-and-solve-mazes-672285723c96
def find_path(maze):
    # BFS algorithm to find the shortest path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (pos[0], pos[1])
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

print(len(path))


# %% PART 2
# import networkx as nx
size=71
# size=7
mat = np.zeros((size, size))

pos =(0,0)
end_pos=(size-1,size-1)

c=0
with open('input.txt') as f:
    for line in f:
        print(c)
        col, row = line.rstrip().split(',')
        col = int(col)
        row = int(row)
        
        mat[row, col] = 1
        path = find_path(mat)
        if path is None:
            break
        c=c+1

print(col, row)


# %%
