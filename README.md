# Advent of code

This repository contains my personal solutions to the **Advent of Code** challenges across various years.  
I use this repository as a collection of notes, primarily for my reference, and to document algorithmic cases that may prove useful in the future.  

Feel free to browse or use the solutions as inspiration, but note that this is intended to serve as a personal resource rather than a polished or optimized codebase.  


# 2024
My solutions to [Advent of code 2024](https://adventofcode.com/2024/) in python.

| Day number | Stars won | Brief strategy description |
| :---:         |     :---:      |          :--- |
| 01   | ⭐ ⭐ |  value sorting and list comprehension |
| 02   | ⭐ ⭐ |   |
| 03   | ⭐ ⭐ |  Regex findall() |
| 04   | ⭐ ⭐ |  Searched for "XMAS" and "SAMX" in horizontal, vertical and diagonal. For diagonal I used `np.diagonal(mat, offset=i)` |
| 05   | ⭐ ⭐ |  I used __topological sorting__ in the second part. I made a Graph given the rules subsetted to the updates list (otherwise it was a cyclic graph and topological sort couldn't work) |
| 06   | ⭐ | |
| 07   | ⭐ | I had to build a __binary tree recursion__ function that tries to divide or to subtract the right most number to the solution. This avoid to use a brute force solution of all possible combinations, since I check whether the right most number is a divisor of the solution, if it's not, I only need to use the subtraction, update the result and repeat. |
| 08   | ⭐ ⭐ | I looped for each unique type of antenna and computed the distance between them. Just simple distance operators within numpy arrays |
| 09   | ⭐ | |
| 10 | ⭐ ⭐ | Thanks to day 07 I learned how to properly use a __binary tree recursion__ and I was really happy to apply it again here! In the first part, when I reached the 9, I transformed into a 10 so that I would not count it again froma nother trail. Part 2 was just removing this condition so that I could count all the trails. |
| 11 |  ⭐ ⭐  | I also used recursion in here. I discovered this magic function decorator `@lru_cache(maxsize = None)` that sped up the computation. |
| 12 |  ⭐  | Since there where different regions with the same values I used `scipy.ndimage import label` so that different clusters had different values. Then with `np.where(m==cell)` I selected only a single cluster and looping through the coordinates in the cluster, I computed the euclidian distance and if it was 1, then the two cells where sharing an edge. I finally computed the perimeter such as 4•nodes-shared_edges. |
| 13 |  ⭐ ⭐  | This was just the solution of a simple linear system. I computed the formula by hand and plugged it in python. In the second part I just check if the equation give the prize coordinates a posterior, so that I don't have rounding errors. |
| 14 |  ⭐ ⭐  | |
| 15 |  💃  | |
| 16 |  💃 | |
| 17 |  💃  | |
| 18 |  ⭐ ⭐  | |
| 19 |  ⭐ ⭐  | |
| 20 |  ⭐ ⭐  | First I search the path using the same code used in day 18 (BFS algorithm). Then for first part I computed __Manhattan distance__ between each point in path, and kept only those with distance=2. Then I filtered out when the gain in steps was>=100. Same for part 2 but I kept points with Manhattan distance <=20  |
| 21 | 💃 | |
| 22 | 💃 | |
| 23 |  ⭐ ⭐  | Super useful the `nx.find_cliques` function to find fully connected subgraph. |
| 24 |  ⭐  | |
| 25 | 💃 | |

## 2023
My solutions to [Advent of code 2023](https://adventofcode.com/2023/) in python.

| Day number | Stars won | Brief strategy description |
| :---:         |     :---:      |          :--- |
| 01   | ⭐ ⭐     |  - I used [word2number](https://pypi.org/project/word2number/) library to transform words to numbers <br> - In cases such as __"oneight"__ where I need to take the last one, I reversed the whole string and took the first reversed number. In other words it's like evaluating the string from right to left and looking for reversed words (from "eight" to "thgie").    |
| 02     | ⭐ ⭐       |  Brute force I guess    |
| 03 | ⭐ ⭐ | I used __signal.convolve2d()__ function to inspect the nearest points around a gear (3x3 convolution) |
| 04 | ⭐ ⭐ | I tried with recursive function but it took too long. Then I found out the solution could be found in a "arithmetically" simpler way |
| 05 | ⭐ | I could not find an efficient strategy to solve this |
| 06 | | 💃 |
| 07 | ⭐ ⭐ |  The function __np.lexsort()__ was super handy here to order a numpy array by a column first, then another one and so on. |
| 08 | ⭐ ⭐ | Least common multiplier |
| 09 |  | 💃 |
| 10 |  | 💃 |
| 11 |  ⭐ ⭐ | Manhattan distance. I took account of the universe expansion when computing the distance. In this way I did not filled up my computer's memory by expanding _a priori_ |
| 12 |  | 💃 |
| 13 | ⭐ ⭐ | - Made use of __np.flip()__ function to compare similarity between a matrix and a mirrored version of the same. <br> - Horizontal reflection is just vertical reflection of the transposed matrix, so I used the same function.
| 14 | ⭐ | First part was ok, second part... I don't know much about cycle detection.