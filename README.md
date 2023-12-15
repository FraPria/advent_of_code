# Advent of code

My solutions to [Advent of code 2023](https://adventofcode.com/2023/) in python.

| Day number | Stars won | Brief strategy description |
| :---:         |     :---:      |          :--- |
| 01   | ⭐ ⭐     |  - I used [word2number](https://pypi.org/project/word2number/) library to transform words to numbers <br> - In cases such as __"oneight"__ where I need to take the last one, I reversed the whole string and took the first reversed number. In other words it's like evaluating the string from right to left and looking for reversed words (from "eight" to "thgie").    |
| 02     | ⭐ ⭐       |  Brute force I guess    |
| 03 | ⭐ ⭐ | I used __signal.convolve2d()__ function to inspect the nearest points around a gear (3x3 convolution) |
| 04 | ⭐ ⭐ | I tried with recursive function but it took too long. Then I found out the solution could be foound in a "arithmetically" simpler way |
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