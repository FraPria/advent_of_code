# %%
import numpy as np
import math


# %%
sol_list = []
numb_list = []
with open('input.txt') as f:
    for line in f:
        sol_list.append(line.rstrip().split(":")[0])
        numb_tmp = line.rstrip().split(": ")[1].split(" ")
        numb_list.append(list(map(int, numb_tmp)))

# %% PART 1
# --> recursive tree.
def tree(s, n):
    if (len(n)==1):
        return (n[0]==s) # If the last number after having done all the operation is equal to the resulting number, 
                         # the operations are valid
    else: 
        if s % n[-1]!=0:
            # last number is not a divider --> I can only subtract it
            subtract_Tree = tree(s-n[-1], n[:-1])
            divide_Tree = False
        else:
            # last number is a divider --> I can either divide it or subtract it
            divide_Tree = tree(s/n[-1], n[:-1])
            subtract_Tree = tree(s-n[-1], n[:-1])
            
    return (subtract_Tree) | (divide_Tree)
    

is_valid = []
solution = 0
for i in range(len(sol_list)):
    numb = numb_list[i]
    sol = int(sol_list[i])

    res = tree(sol, numb)
    is_valid.append(res)
    if res==True:        
        solution = solution + int(sol_list[i])

print(solution)


# %% PART 2

def tree(s, n):
    if (len(n)==1):
        return (n[0]==s) # If the last number after having done all the operation is equal to the resulting number, 
                         # the operations are valid
    elif (s<=0):
        return False    
    else: 
        if s % n[-1]!=0:
            # last number is not a divider --> I can only subtract it
            subtract_Tree = tree(s-n[-1], n[:-1])
            divide_Tree = False
            concat_Tree = False
        else:
            # last number is a divider --> I can either divide it or subtract it
            divide_Tree = tree(s/n[-1], n[:-1])
            subtract_Tree = tree(s-n[-1], n[:-1])
            concat_Tree = False
            

        if  len(n)>2:
            concat = int(str(n[-2]) + str(n[-1]))
            concat_Tree = tree(s, numb[:-2] + [concat])

            
    return (subtract_Tree) | (divide_Tree) | (concat_Tree) 

# RecursionError: maximum recursion depth exceeded while calling a Python object


is_valid = []
solution = 0
for i in range(len(sol_list)):
    print(i)
    numb = numb_list[i]
    sol = int(sol_list[i])

    res = tree(sol, numb)
    is_valid.append(res)
    if res==True:        
        solution = solution + int(sol_list[i])

print(solution)
s# %%

# %%
