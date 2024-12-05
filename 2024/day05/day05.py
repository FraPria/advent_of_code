# %%
import numpy as np
import re 
import networkx as nx
import math
import matplotlib.pyplot as plt

# %% 
rules = []
updates = []
with open('input.txt') as f:
    for line in f:
        if "|" in line:
            rules.append(line.rstrip().split("|"))
        if "," in line:
            updates.append(line.rstrip().split(","))


# %% PART 1
middle_terms_lst = []
rules_list = [ '|'.join(r) for r in rules ]

for i in range(len(updates)):
    pairs = [ '|'.join([updates[i][j],updates[i][j+1]]) for j in range(len(updates[i])-1) ]
    is_valid = [ p in rules_list for p in pairs]
    if all(is_valid):
        middle = math.floor(len(updates[i])/2)
        middle_terms_lst.append(int(updates[i][middle]))

print(sum(middle_terms_lst))


# %% PART 2
# I will create a directed graph and then use topological sort
middle_terms_lst = []

for i in range(len(updates)):
    sub_idx = [ idx  for idx, r in enumerate(rules) if (r[0] in updates[i]) & (r[1] in updates[i]) ]
    edges1 = [rules[idx] for idx in sub_idx]
    nodes1 = list(set(([ r[0] for r in edges1] + [ r[1] for r in edges1])))
    G1 = nx.DiGraph()
    G1.add_nodes_from(nodes1)
    G1.add_edges_from(edges1)
    toposort = list(nx.topological_sort(G1))

    # dictionary of sorted values and their index (0, 1, 2...)
    sortdict = {}
    for index, element in enumerate(toposort):
        sortdict[element] = index

    # replace elements in updates with their index of the topological sorting
    idx_list = [sortdict[key] for key in updates[i]]
    if sorted(idx_list) != idx_list:
        ordered_updates = list(sortdict.keys())
        middle = math.floor(len(ordered_updates)/2)
        middle_terms_lst.append(int(ordered_updates[middle]))

print(sum(middle_terms_lst))

