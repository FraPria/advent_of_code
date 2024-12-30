# %%
import re
import pandas as pd

# %% PART1: it's just a solution of a linear system
df = pd.DataFrame()
with open('input.txt') as f:
    for line in f:
        print(line.rstrip())
        # print(line)
        if 'Button A:' in line:
            a = re.split('Button A: |X\+|, Y\+|\n', line)[2:4]
        elif 'Button B:' in line:
            b = re.split('Button B: |X\+|, Y\+|\n', line)[2:4]
        elif 'Prize' in line:
            print(re.split('Prize: |X=|, Y=|\n', line)[2:4])
            p = re.split('Prize: |X=|, Y=|\n', line)[2:4]
        elif line=='\n':
            # print(line) 
            tmp = pd.DataFrame({'A_x': [a[0]], 'A_y': [a[1]],
                                'B_x': [b[0]], 'B_y': [b[1]],
                                'Prize_x': [p[0]], 'Prize_y': [p[1]]
                            })
            df = pd.concat([df, tmp])

tmp = pd.DataFrame({'A_x': [int(a[0])], 'A_y': [int(a[1])],
                    'B_x': [int(b[0])], 'B_y': [int(b[1])],
                    'Prize_x': [int(p[0])], 'Prize_y': [ int(p[1]) ]
                })
df = pd.concat([df, tmp])
df.reset_index(inplace=True)
df['A_x'] = pd.to_numeric(df['A_x'])
df['A_y'] = pd.to_numeric(df['A_y'])
df['B_x'] = pd.to_numeric(df['B_x'])
df['B_y'] = pd.to_numeric(df['B_y'])
df['Prize_x'] = pd.to_numeric(df['Prize_x'])
df['Prize_y'] = pd.to_numeric(df['Prize_y'])


# %% PART1: it's just a solution of a linear system
# N multiplier of A, M multiplier of B
tokens = 0
for r in range(len(df)):
    row = df.loc[r].copy()
    N = (row['Prize_y']-(row['B_y']*row['Prize_x'])/row['B_x'])/( row['A_y'] - (row['B_y']*row['A_x'])/row['B_x'] )
    M = (row['Prize_x']-N*row['A_x'])/row['B_x']
    df.loc[r,'N'] = N
    df.loc[r,'M'] = M
    if (round(N)==round(N,6)) & (round(M)==round(M,6)): # check if the multiplier are integers
        df.loc[r,'possible'] = True
        tokens = tokens + N*3+M*1

print(tokens)

# %% PART2: check a posterior if the equation with the computed N,M are valid. 
# # The if used in the first part could contain rounding errors.
tokens = 0
df['P2_x'] = 10000000000000+df['Prize_x']
df['P2_y'] = 10000000000000+df['Prize_y']
df['possible']=False
for r in range(len(df)):
    row = df.loc[r].copy()
    N = (row['P2_y']-(row['B_y']*row['P2_x'])/row['B_x'])/( row['A_y'] - (row['B_y']*row['A_x'])/row['B_x'] )
    M = (row['P2_x']-N*row['A_x'])/row['B_x']
    df.loc[r,'N'] = N
    df.loc[r,'M'] = M

# 104958599303720
df['check_x']=(round(df['N'])*df['A_x']+round(df['M'])*df['B_x']==df['P2_x']) & (df['N']>0) & (df['M']>0)
df['check_y']=(round(df['N'])*df['A_y']+round(df['M'])*df['B_y']==df['P2_y'])  & (df['N']>0) & (df['M']>0)

valid = df.loc[(df['check_x']) & (df['check_y'])].copy()
valid.reset_index(inplace=True)

tokens = sum(valid['N']*3+valid['M'])

print('{:.2f}'.format(tokens))
# %%
