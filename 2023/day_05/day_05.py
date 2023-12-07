
# %%
import re
import numpy as np
import os
import pandas as pd

# 
os.chdir('/Users/francesca/Desktop/coding_shit/advent_of_code/2023/day_05')

# %% 
def get_destination(s,n):
    sub_df = df[(df['source_label']==s) & (df['source_start']<=n) & (df['source_end']>=n) ]
    if len(sub_df)>0:
        gap = int(n-sub_df['source_start'])
        res_d = sub_df['destination_start']+gap
        res_d = int(res_d.values)
    else: 
        res_d = n
    return res_d

# %%
with open('day_05_input.txt') as file:
# with open('day_05_test.txt') as file:
    wordlist = file.read().splitlines()

# %%
df = pd.DataFrame(columns = ['source_start','source_end','destination_start','destination_end','source_label','destination_label'])
# with open('day_05_test.txt') as file:
# with open('day_05_input.txt') as file:
#     for line in file:

# sources_interval = dict({'seed':range(0)})
for line in wordlist:
# for line in open('day_05_input.txt','r'):
    print(line)
    if line=='':
        next
    elif line.startswith('seeds:'):
        line = line.replace('\n', '')
        seeds_vec = re.split('\:|\ ',line)[2::]
        
    elif line[0].isalpha():
        source = re.split(r'\-|\ ', line)[0]
        destination = re.split(r'\-|\ ', line)[2]
        print(source + ' ' + destination)
    
    elif line[0].isdigit():
        steps = int(re.split('\ ',line)[2])
        source_start = int(re.split('\ ',line)[1])
        destination_start = int(re.split('\ ',line)[0])

        tmp = pd.DataFrame({'source_start': int(source_start),
                            'source_end': int(source_start+steps-1),
                            'destination_start': int(destination_start),
                            'destination_end': int(destination_start+steps-1),
                            'source_label': source, 'destination_label': destination
                        }, index = [0]
                        )
        df = pd.concat([df,tmp],axis=0)
        

# %%

# 	source_start	source_end	destination_start	destination_end	source_label	destination_label
# 0	1235603193	1478217469	1270068015	1512682291	seed	soil
# ...	...	...	...	...	...	...
# 0	2629034942	2630924016	3431458956	3433348030	humidity	location
# 0	2751566862	2878291221	4168242936	4294967295	humidity	location


# %% Part 1 solution
i = 0 
destination_vec = np.zeros(len(seeds_vec))
for seed in seeds_vec:
    n = int(seed)
    for s in ['seed','soil','fertilizer','water','light','temperature','humidity']:
        n = get_destination(s, n)
    destination_vec[i] = n
    i += 1

print(min(destination_vec))


# %% Part 2 solution
seed_start = np.array(list(map(int, seeds_vec[::2])))
rang = np.array(list(map(int, seeds_vec[1::2])))

# seeds_ranges = range(0)
# for i in range(len(seed_start)):
#     seeds_ranges = seeds_ranges + range(int(seed_start[i]), int(rang[i]))

seed_ranges = pd.DataFrame({'start': seed_start, 
                            'end':  seed_start+rang})


seed_ranges.to_csv('seeds.csv')
df.to_csv('all.csv')

# %%
r1 = seed_ranges
r2 = df[df['source_label']=='seed']
r1 = r1.reset_index(drop=True)
r2 = r2.reset_index(drop=True)
res = pd.DataFrame()
for i in range(len(r1)):
    for j in range(len(r2)):
        start1 = r1.loc[i]['start']
        start2 = r2.loc[j]['source_start']
        end1 = r1.loc[i]['end']
        end2 = r2.loc[j]['source_end']
        # if ((end1 < start2) | (end2 < start1)):
        #     result = []
        intersect_range = [max(start1, start2), min(end1, end2)]
        if intersect_range[0]>intersect_range[1]:
            res = res + r1
        elif start1<intersect_range:
            res = res
            


# %%
# i = 0
# s = 'seed'
# seed_ranges[i]


# def intersect_ranges(r1, r2):

#     inter = [max(r1[0], r2[0]), min(r1[1], r2[1])]
#     return inter

# sub_df = df[(df['source_label']==s)]
# sub_df = sub_df.reset_index()
# for r in len(sub_df):
#     intersect_ranges( seed_ranges.loc[i].values, sub_df.loc[r][['source_start','source_end']])


# %%
seed_start = list(map(int, seeds_vec[::2]))
rang = list(map(int, seeds_vec[1::2]))

new_seeds = []
for i in range(len(seed_start)):
    print(str(i)+ ' ' + str(len(seed_start)))
    new_seeds = new_seeds + list(range(int(seed_start[i]), int(seed_start[i]) + int(rang[i])))

i = 0 
destination_vec = np.zeros(len(new_seeds))
for seed in new_seeds:
    print(str(i) +'  /  ' +str(len(new_seeds) ))
    n = int(seed)
    for s in ['seed','soil','fertilizer','water','light','temperature','humidity']:
        n = get_destination(s, n)
    destination_vec[i] = n
    i += 1

print(min(destination_vec))
# %%
