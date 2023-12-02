# %%
# The Elf would first like to know which games would have been possible 
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
import pandas as pd
import os 
import re
import numpy as np

# %% Create dataframe
os.chdir('/Users/francesca/Desktop/coding_shit/advent_of_code/2023/')

df = pd.DataFrame( columns = ['game', 'round', 'elements'])
with open('day_02_input.txt') as file:
# with open('day_02_test.txt') as file:
    for line in file:
        list_line = re.split(': |; ', line)
        for i in range(len(list_line)-1):
            new_row = {'game':  re.split(' |:', line)[1], 
                        'round': i+1, 
                        'elements': list_line[i+1] }
            df = df.append(new_row, ignore_index=True)

df['elements'] = df['elements'].str.replace(r'\n','') 

# %% Step 1
def round_valid(input_string):
    listed = input_string.split(', ')
    # res = pd.DataFrame(np.zeros((1, 3)), columns = ['red', 'green', 'blue'])
    valid = [True, True, True]
    for e in listed:
        if ('red' in e) & (int(e.split(' ')[0])>12) :
            valid[0]=False
        elif ('green' in e) & (int(e.split(' ')[0])>13) :
            valid[1]=False
        elif ('blue' in e) & (int(e.split(' ')[0])>14) :
            valid[2]=False
    return all(valid)


df['valid_round'] = df.apply(lambda row: round_valid(row['elements']), axis=1 )

results = df.groupby('game').all()['valid_round']

solution1 = np.sum((results[results].index.values).astype('int'))
print('solution of step 1 is: ' + str(solution1))


# %% Step 2
def list_to_color_mat(input_string):
    listed = input_string.split(', ')
    # res = pd.DataFrame(np.zeros((1, 3)), columns = ['red', 'green', 'blue'])
    res = np.zeros((1, 3))
    for e in listed:
        if 'red' in e:
            res[0,0] = e.split(' ')[0]
        elif 'green' in e:
            res[0,1] = e.split(' ')[0]
        elif 'blue' in e:
            res[0,2] = e.split(' ')[0]
    return res

new_df = pd.DataFrame(columns = ['red', 'green', 'blue'])
for row in range(len(df)):
    tmp = list_to_color_mat(df.iloc[row]['elements'])
    new_df = new_df.append(pd.DataFrame(tmp, columns = ['red', 'green', 'blue']))
new_df = new_df.reset_index()

df = pd.concat([df, new_df], axis=1)

# %%
results = df.groupby('game').max()[['red','green','blue']]
solution2 = np.sum(results['red']*results['green']*results['blue'])
print('solution of step 2 is: ' + str(solution2))





# %%
