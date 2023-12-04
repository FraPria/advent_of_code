# %% 
import re
import numpy as np
from scipy import signal


# %%
def clean_strings(input):
    input = re.split(r'\ |\ \ ', input)
    output = [x for x in input if x != '']
    return output

# =====================================
# %%
result1 = 0
cards_match = []
# with open('day_04_test.txt') as file:
with open('day_04_input.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        cards = re.split(r': ', line)[1]
        winning = re.split(r'\|', cards)[0]
        winning = clean_strings(winning)

        mine = re.split(r'\|', cards)[1]
        mine = clean_strings(mine)

        n_match = sum([item in mine for item in winning])
        cards_match.append(n_match)
        if n_match!=0:
            print(2**(n_match-1))
            result1  = result1 + 2**(n_match-1)
        # txt = [line.rstrip() for line in file]
    
print('Result of Part 1 = ' + str(result1))


# =====================================
# %% Part 2

copies = np.ones(len(cards_match)) #  'int' object is not iterable
for c in range(len(cards_match)):
    w = cards_match[c]
    copies[(c+1):(c+1+w)] += copies[c] 
print('Result of Part 2 = ' + str(sum(copies)))

# # =====================================
# # %% Part 2 (recursion test: spoiler, works for test but not full input. Heavy computation)
# copies = np.zeros(len(cards_match))

# def get_copies(v, copies, pos):
#     for i in range(pos, len(v)):
#         n = v[i]
#         if len(copies[(i+1):(i+1+n)])==0:
#             return np.zeros(len(copies))
#         else:
#             copies[(i+1):(i+1+n)] += 1    
#             copies += get_copies(v, copies, pos=i+1)
#             # print(copies)
#     return(copies)
     
# a = get_copies(cards_match, copies, 0) # non so perché non funzia a.
# print(a)

# result2 = sum(copies)+len(copies)
# print('Result of Part 2 = ' + str(result2))


# %%
