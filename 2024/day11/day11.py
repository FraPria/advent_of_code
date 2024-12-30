# %% 
text = []
with open('input.txt') as f:
    for line in f:
        text.append(line.rstrip().split(' '))

text = text[0]

# %% PART 1

def apply_rules(text):
    newlist = []
    for i in text:
        if i=='0':
            newlist.append('1')
        elif len(i) % 2 ==0:
            left, right = i[:int(len(i)/2)], i[int(len(i)/2):]
            newlist.append(left)
            newlist.append(str(int(right)))
        else:
            newlist.append(str(2024*int(i)))
    return newlist

newlist = text.copy()

for j in range(25):
    newlist = apply_rules(newlist)

len(newlist)

# %% PART 2
# avoid doing the full list, do recursion instead and sum up the stones at the end
from functools import lru_cache

@lru_cache(maxsize = None) # unlimited cache
def apply_rules2(t, depth, bottom):
    s = 0
    if depth==bottom:
        s = s+1
        return(s)
    
    for idx in range(len(t)):
        i = t[idx]
        s_tmp = 0
        if i=='0':
            s_tmp = s_tmp+apply_rules2(tuple(['1']), depth+1, bottom)
        elif len(i) % 2 ==0:
            left, right = i[:int(len(i)/2)], i[int(len(i)/2):]
            s_left = apply_rules2(tuple([left]), depth+1, bottom)
            s_right = apply_rules2(tuple([str(int(right))]), depth+1, bottom)
            s_tmp = s_tmp + s_right +s_left
        else:
            s_tmp = s_tmp+apply_rules2(tuple([str(2024*int(i))]), depth+1, bottom) 
        s = s+s_tmp   

    return s

apply_rules2(tuple(text.copy()), 0, bottom=75)
    

# %%
