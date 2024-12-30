# %%
import numpy as np
import re 
import networkx as nx

# %%

edge_list = []
with open('input.txt') as f:
    for line in f:
        edge_list.append(line.rstrip().split("-"))

G=nx.from_edgelist(edge_list  )
# nx.draw(G)

# %% PART 1
triplets = []
n0='qp'

for n0 in G.nodes:
    for n1 in G.neighbors(n0): # neighbors of point n0
        for n2 in G.neighbors(n1): # neighbors of neighbors of point n0
            if n2 in G.neighbors(n0): # if they are also neighbors of n0 --> I have a triplet
                triplets.append([n0, n1, n2])

# there are repeated triplets in different order. I take only unique triplets
triplets = [tuple(sorted(l)) for l in triplets]
triplets = list(set(triplets))

idx = list(set([ idx for idx, t in enumerate(triplets) for node in t  if node.startswith('t')   ]))
triplets_t = [t for i, t in enumerate(triplets) if i in idx]


len(triplets_t)

# %% PART 2

clique = list(nx.find_cliques(G))
clique = [tuple(sorted(l)) for l in clique]
max_clique = max([ len(c) for c in clique])
sol2 = ','.join([ c for c in clique if len(c)==max_clique][0])

print(sol2)
# bc,bf,do,dw,dx,ll,ol,qd,sc,ua,xc,yu,zt


# %%
