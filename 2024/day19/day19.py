# %%
import re

# %%
design = []
with open('input.txt') as f:
    for line in f:
        if ',' in line:
            pieces = re.split(', |\n', line)[:-1]
        elif '\n' == line:
            next
        else:
            design.append(line.replace('\n',''))

# %%
pieces = sorted(pieces, key=len, reverse=True)

# %% PART 1
from functools import lru_cache

@lru_cache(maxsize = None)
def search_substring(pieces, word):
    if len(word)==0:
        return len(word) # if the word is zero length, it means I covered it with the substring
    else:
        substring_list = [ substring for substring in pieces if word.startswith(substring)  ]

        residual = len(word)
        partial_residual = []
        
        for substring in substring_list:
            s = word

            # if s.startswith(substring):
            s = s[(len(substring)):] # remove first N characters
            partial_residual.append(search_substring(pieces, s)) # after removing the substring, how long is the word?
            residual = min(partial_residual)
    return residual


# search_substring(pieces, design[5])

covered = []
for i in range(len(design)):
    l = search_substring(tuple(pieces), design[i])
    print(i)
    covered.append(l==0)

sum(covered)


# %% PART 2
from functools import lru_cache

@lru_cache(maxsize = None)
def search_substring2(pieces, word):
    if len(word)==0:
        # success = success+1 
        return 1  
    else:
        substring_list = [ substring for substring in pieces if word.startswith(substring)  ]
        
    success_count = 0

    # Explore all possible paths and sum up successful ones
    for substring in substring_list:
        remaining_word = word[len(substring):]  # 
        success_count += search_substring2(pieces, remaining_word)

    return success_count
        
    #     for substring in substring_list:
    #         s = word
    #         s = s[(len(substring)):] # remove first N characters
    #         success = search_substring2(pieces, s, success) 

    #         print(substring, success)
    # return success



success = 0
for i in range(len(design)):
    print(i)
    num_success = search_substring2(tuple(pieces), design[i])
    success = success + num_success 

print(success)

# %%
