# %% import
import pandas as pd

# %% part1 ==========================
df = pd.read_table('day01.txt', sep='   ', header=None)
df.columns=['a','b']

df2 = pd.concat([df.a.sort_values().reset_index(drop=True), 
                 df.b.sort_values().reset_index(drop=True)], axis=1)
df2['distance'] = abs(df2['a'] - df2['b'])

ans1 = df2['distance'].sum()
print('First answer: ' + str(ans1))


# %% part2 ==========================
ans2 = sum([ a*sum(df['b']==a) for a in df['a'].tolist()])
print('Second answer: ' + str(ans2))

# %%
