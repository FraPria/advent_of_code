# %%
import numpy as np
from queue import Queue


# %%
with open('input.txt') as f:
    mat = [list(line.rstrip()) for line in f]

mat = np.array(mat)
# %%
pos = np.where(mat=='S')
end_pos = np.where(mat=='E')

# def move(m, pos, direction, score):
#     if m[pos[0], pos[1]+1]=='.':
#         m[pos[0], pos[1]+1] = '#'
#         if direction =='up':
#             score = score+1
#         else:
#             score = score+1000
#         move(m, pos[0], pos[1]+1,'up', score)



# %%

maze = mat.copy()
maze[maze=='#'] = 1
maze[maze!='#'] = 0
maze = maze.astype(np.float)

# %%
# https://medium.com/@msgold/using-python-to-create-and-solve-mazes-672285723c96
def find_path(maze):
    # BFS algorithm to find the shortest path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (pos[0][0], pos[1][0])
    end = (end_pos[0][0], end_pos[1][0])
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

find_path(maze)
# %%
