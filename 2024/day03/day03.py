#%%

import re

# %% PART 1
# with open('input.txt', 'r') as file:
#     txt = [line.rstrip() for line in file]

pt = []
prod = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        l = line.strip()
        x = re.findall("mul\(\d+,\d+\)", l)
        # pt.append(re.findall("mul\(\d+,\d+\)", l))
        d1 = [ int(i.replace('mul(', '').replace(')','').split(',')[0]) for i in x ]
        d2 = [ int(i.replace('mul(', '').replace(')','').split(',')[1]) for i in x ]
        
        prod.append(sum([ d1[i]*d2[i] for i in range(len(d1))]) )

print(sum(prod))



# %% PART 2

pt = []
prod = []
lst = []
txt = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        l = line.strip()
        x = re.findall("mul\(\d+,\d+\)|don\'t\(\)|do\(\)", l)
        lst.append(x)
        txt.append(l)

# flatten the list
x = [item for sublist in lst for item in sublist]
action = 'multiply'
debug = []
products = []
for i in x:
    if i=="don't()":
        action = 'nothing'
        products.append(0)
    elif i=="do()":
        action = 'multiply'
        products.append(0)
    
    if (action=='multiply') & (i!="do()"):
        d1 = int(i.replace('mul(', '').replace(')','').split(',')[0]) 
        d2 = int(i.replace('mul(', '').replace(')','').split(',')[1])
        products.append(d1*d2)
        prod.append(d1*d2)
    debug.append(action)
    # print(sum(products))

print(sum(prod)) 


[' '.join(i) for i in zip(x,debug)]

# %%
