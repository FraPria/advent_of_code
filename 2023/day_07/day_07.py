# %%
import re
import numpy as np
import os
import pandas as pd

# %%


# ordering = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
ordering_dict = {'A':1, 'K':2, 'Q':3, 'J':4, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12, '2':13}

# %%


# poker = np.empty((0,5))
poker = []
bids = []

# with open('day_07_test2.txt') as file:
# with open('day_07_test.txt') as file:
with open('day_07_input.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        list_line = list(re.split('\ ', line)[0])
        bids.append(re.split('\ ', line)[1])

        tmp = [ordering_dict[l] for l in list_line] # use dictionary to transform symbols into ordered numbers
        poker.append(tmp)


# %% Part 1
poker = np.array(poker)
bids = np.array(bids)
unique_cards = list(map(set, poker))
# n_uniq = [len(x) for x in unique_cards]
table_cards = [ np.unique(row, return_counts=True)[1] for row in poker ]

# %%

first_order = []
for i in table_cards:
    if len(i)==1:
        # Five of a kind
        first_order.append(1)
    elif (len(i)==2) & (max(i)==4):
        #four of a kind
        first_order.append(2)
    elif  (len(i)==2) & (max(i)==3):
        # full
        first_order.append(3)
    elif (len(i)==3) & (max(i)==3):
        # three of a kind
        first_order.append(4)
    elif (len(i)==3) & (max(i)==2):
        # two pairs
        first_order.append(5)
    elif len(i)==4:
        # One pair
        first_order.append(6)
    else:
        first_order.append(7)

# %%
# a = np.array(first_order)==7
# poker[a,:]

ordered_bids = []
ordered_poker = []
for o in range(1,8):
    print(o)
    belong_to_o = [item==o for item in first_order]
    tmp_poker = poker[belong_to_o]
    tmp_bids =  bids[belong_to_o]
    if len(tmp_poker)==0:
        next
    else:
        tmp_idx = np.lexsort((tmp_poker[:,4], tmp_poker[:,3], tmp_poker[:,2], tmp_poker[:,1], tmp_poker[:,0])) # indeces of rows ordered by first column 0 then 1, and so on
        ordered_bids.append(tmp_bids[tmp_idx].tolist())
        ordered_poker.append(tmp_poker[tmp_idx,:])

ordered_bids = [item for sublist in ordered_bids for item in sublist]
print(ordered_poker)
print(ordered_bids)
# idx = np.lexsort((poker[:,0],poker[:,1], poker[:,2], poker[:,3], poker[:,4])) # indeces of rows ordered by first column 0 then 1, and so on
ordered_bids = [int(item) for item in ordered_bids]
# %%
solution1 = sum(ordered_bids[::-1]*np.array(list(range(1, len(ordered_bids)+1 ) )))
print(solution1)
# %%

# =============================
# %% Part 2
ordering_dict = {'A':1, 'K':2, 'Q':3, 'T':4, '9':5, '8':6, '7':7, '6':8, '5':9, '4':10, '3':11, '2':12, 'J':13}

poker = []
bids = []

# with open('day_07_test2.txt') as file:
# with open('day_07_test.txt') as file:
with open('day_07_input.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        list_line = list(re.split('\ ', line)[0])
        bids.append(re.split('\ ', line)[1])

        tmp = [ordering_dict[l] for l in list_line] # use dictionary to transform symbols into ordered numbers
        poker.append(tmp)

# %% 
poker = np.array(poker)
bids = np.array(bids)
unique_cards = list(map(set, poker))
table_cards = [ np.unique(row, return_counts=True)[1] for row in poker ]

jokers_num = []
for r in range(len(poker)):
    jokers_num.append(sum(poker[r,:]==13))

# %%
c = 0
first_order = []
for i in table_cards:
    if len(i)==1:
        # Five of a kind
        first_order.append(1)
    elif (len(i)==2) & (max(i)==4):
        #four of a kind
        first_order.append(2)
    elif  (len(i)==2) & (max(i)==3):
        # full
        first_order.append(3)
    elif (len(i)==3) & (max(i)==3):
        # three of a kind
        first_order.append(4)
    elif (len(i)==3) & (max(i)==2):
        # two pairs
        first_order.append(5)
    elif len(i)==4:
        # One pair
        first_order.append(6)
    else:
        first_order.append(7)
    c = c + 1


# %%
# from itertools import compress
new_first_order = first_order
# # 1 joker and 4 of a kind --> +1
# idx = [(jokers_num[i]==1) & (first_order[i]==2)  for i in range(len(jokers_num))] 
# new_first_order[idx] = first_order[idx]+1

for i in range(len(jokers_num)):
    # 1 JOKER --------
    if (jokers_num[i]==1) & ((first_order[i]==2) | (first_order[i]==7) ): 
        # - four of a kind and a Joker --> five of a kind -1  AAAAJ 
        # - all different and a Joker --> single pair -1 ABCDJ
        new_first_order[i] = first_order[i]-1
    elif (jokers_num[i]==1) & ((first_order[i]==4) | (first_order[i]==5) | (first_order[i]==6)):
        # - three of a kind and a Joker --> 4 of a kind -2
        # - two pairs and a joker --> full -2
        # - a single pair --> three of a kind -2
        new_first_order[i] = first_order[i]-2

    # 2 JOKERS --------
    elif (jokers_num[i]==2) & ((first_order[i]==3) | (first_order[i]==6 )):
        # - from full to five of a kind
        # - from single pair to tris
        new_first_order[i] = first_order[i]-2
    elif (jokers_num[i]==2) & (first_order[i]==5 ):
        # - from two pairs to four of a kind AAQJJ
        new_first_order[i] = first_order[i]-3

    # 3 JOKERS --------
    elif (jokers_num[i]==3) & ((first_order[i]==3) | (first_order[i]==4 )):
        # - from a full to five of a kind: AAJJJ
        # - from a tris to four of a kind: AQJJJ
        new_first_order[i] = first_order[i]-2
    
    # 4 JOKERS --------
    elif (jokers_num[i]==4) & (first_order[i]==2):
        new_first_order[i] = first_order[i]-1
    



# %%
# a = np.array(first_order)==7
# poker[a,:]

ordered_bids = []
ordered_poker = []
for o in range(1,8):
    print(o)
    belong_to_o = [item==o for item in new_first_order]
    tmp_poker = poker[belong_to_o]
    tmp_bids =  bids[belong_to_o]
    if len(tmp_poker)==0:
        next
    else:
        tmp_idx = np.lexsort((tmp_poker[:,4], tmp_poker[:,3], tmp_poker[:,2], tmp_poker[:,1], tmp_poker[:,0])) # indeces of rows ordered by first column 0 then 1, and so on
        ordered_bids.append(tmp_bids[tmp_idx].tolist())
        ordered_poker.append(tmp_poker[tmp_idx,:])

ordered_bids = [item for sublist in ordered_bids for item in sublist]
print(ordered_poker[::-1])
print(ordered_bids[::-1])
# idx = np.lexsort((poker[:,0],poker[:,1], poker[:,2], poker[:,3], poker[:,4])) # indeces of rows ordered by first column 0 then 1, and so on
ordered_bids = [int(item) for item in ordered_bids]
# %%
solution2 = sum(ordered_bids[::-1]*np.array(list(range(1, len(ordered_bids)+1 ) )))
print(solution2)
# %%
