# %%
import numpy as np

# %% Import text to numpy array matrix
with open('input.txt') as f:
    text = [ list(line.rstrip()) for line in f]
    text = [ int(a) for a in text[0]]


# %%
lst_blocks = []
lst_gaps = []
expansion = []
idx_lst_blocks = []
# idx_lst_gaps = []
j = 0
k = 0
for i in range(len(text)):
    t = text[i]
    if i % 2 ==0 :
        lst_blocks.append([j] * t)
        idx_lst_blocks.append(list(range(k, k+t)))
        expansion.append([j] * t)
        j = j + 1
    else:
        lst_gaps.append(['.'] * t)
        # idx_lst_gaps.append(list(range(k, k+t)))
        expansion.append(['.'] * t)

lst_blocks_flat = [item for items in lst_blocks for item in items]
expansion = [item for items in expansion for item in items]

# %%
lst_blocks_flat = [item for items in lst_blocks for item in items]

prod = 0
i = 0
completed = np.zeros(len(expansion))
while len(lst_blocks_flat)!=0:
    if expansion[i]!='.':
        # completed[i] = expansion[i]
        prod = prod+expansion[i]*i
        lst_blocks_flat = lst_blocks_flat[1::] # vado avanti coi blocchi

    else:
        # completed[i] = lst_blocks_flat[-1]
        prod = prod+lst_blocks_flat[-1]*i
        lst_blocks_flat = lst_blocks_flat[:-1]
    i = i+1

# print(sum([ completed[i]*i  for i in range(len(completed))]))
print(prod)

# %%

# %%


# lst_blocks = []
# lst_gaps = []
# # lst = []
# idx_lst_blocks = []
# idx_lst_gaps = []
# j = 0
# k = 0
# for i in range(len(text)):
#     t = text[i]
#     if i % 2 ==0 :
#         lst_blocks.append([j] * t)
#         idx_lst_blocks.append(list(range(k, k+t)))
#         # lst.append([j] * t)
#         j = j + 1
#     else:
#         lst_gaps.append(['.'] * t)
#         idx_lst_gaps.append(list(range(k, k+t)))
#         # lst.append(['.'] * t)
    
#     k = k+t

# lst_blocks_flat = [item for items in lst_blocks for item in items]
# idx_lst_blocks_flat = [item for items in idx_lst_blocks for item in items]

# lst_gaps_flat = [item for items in lst_gaps for item in items]
# idx_lst_gaps_flat = [item for items in idx_lst_gaps for item in items]

# blocks_fixed = lst_blocks_flat[0:(-len(lst_gaps_flat)+2)]
# idx_blocks_fixed = idx_lst_blocks_flat[0:(-len(lst_gaps_flat)+2)]
# blocks_tomove = lst_blocks_flat[(len(lst_gaps_flat)+1)::]

# newlist = np.zeros(len(idx_lst_blocks_flat)+len(idx_lst_gaps_flat))
# for i in range(len(blocks_fixed)):
#     newlist[idx_blocks_fixed[i]] = blocks_fixed[i]

# for i in range(len(blocks_tomove)-1):
#     newlist[idx_lst_gaps_flat[i]] = blocks_tomove[-i-1]

# # fixed_sum = sum([ blocks_fixed[i]*idx_blocks_fixed[i] for i in range(len(blocks_fixed))])
# # moved_sum = sum([ blocks_tomove[-i-1]*idx_lst_gaps_flat[i] for i in range(len(blocks_tomove)) ])

# # too low 275026498682
# print(sum([ i*newlist[i] for i in range(len(newlist))]))


# # %%

# # %%
