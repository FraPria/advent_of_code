# %%
import pandas as pd


# %% PART 1
import re

def check_is_safe(row):
    is_sorted = (row == sorted(row) ) | \
        (row == sorted(row, reverse=True))
    
    diff_el = [abs(int(row[el + 1]) - int(row[el])) for el in range(len(row)-1)]

    is_safe = (is_sorted) & (max(diff_el)<=3) & (min(diff_el)>=1)
    return is_safe

input_list = []
is_safe_list = []

with open('input.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        list_line = list(re.split('\ ', line))
        input_list.append(list(map(int, list_line)))

for i in range(len(input_list)):
    row = input_list[i] 
    is_safe = check_is_safe(row)
    is_safe_list.append(is_safe)

print('First solution: ' + str(sum(is_safe_list)))


# %% PART 2

not_safe_idx =[i for i, x in enumerate(is_safe_list) if  x==False]


is_safe2 = []
for i in not_safe_idx:
    is_safe1 = []
    for j in range(len(input_list[i])):
        row = input_list[i].copy()
        updated_row = [element for idx, element in enumerate(row) if idx != j]
        is_safe = check_is_safe(updated_row)
        is_safe1.append(is_safe)

    is_safe2.append(any(is_safe1))


print('Second solution: ' + str(sum(is_safe_list) + sum(is_safe2)))

# %%
