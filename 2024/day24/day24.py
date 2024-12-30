# %%
import numpy as np
import re 
import pandas as pd

# %% 
dict1 = {}
operations = pd.DataFrame()

with open('input.txt') as f:
    for line in f:
        if ":" in line:
            a = line.rstrip().split(": ")
            dict1[a[0]] =  int(a[1])
        if "->" in line:
            b = re.split(' | -> |\n', line)
            operations = pd.concat([operations,
                     pd.DataFrame({'left': [b[0]],  
                                   'right': [b[2]],
                                   'result': [b[4]],
                                   'operation': [b[1]]                            
                                   })])

operations.reset_index(inplace=True, drop=True)


# %% PART 1

while len(operations)!=0:
    for index, op in operations.iterrows():
        # print(index, len(operations))
        if (op['left'] in dict1.keys()) & (op['right'] in dict1.keys()):
            if op['operation']=='OR':
                res = dict1[op['left']] | dict1[op['right']]
            elif op['operation']=='AND':
                res = dict1[op['left']] & dict1[op['right']]
            elif op['operation']=='XOR':
                res = bool(dict1[op['left']]) != bool(dict1[op['right']])

            dict1[op['result']] = res
            operations = operations.drop(index)
        else:
            next

only_z = {key: value for key, value in sorted(dict1.items(), reverse=True) if key.startswith('z')}
display(only_z)


binary = ''.join([ str(int( value)) for key, value in only_z.items() if key.startswith('z') ])
print('result ', int(binary,2))


# %%
