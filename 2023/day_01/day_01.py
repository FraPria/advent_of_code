
# %%
import os
import re
from word2number import w2n

with open('day_01_input.txt') as file:
    txt = [line.rstrip() for line in file]

# ===============================
# %% Part 1
sumup = 0
two_digits = []
for i in range(len(txt)):
    first = re.findall(r'\d', txt[i])[0] 
    last = re.findall(r'\d', txt[i])[-1]  

    two_digits.append(int(str(first)+str(last)))
    sumup = sumup + two_digits[i]

print(sumup)

# ===============================
# %% Part 2 
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
sumup = 0
two_digits = []
for i in range(len(txt)):
    first = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine|zero', txt[i])[0] 
    last = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez', txt[i][::-1])[0]  
    # to avoid taking the first between overlapping words such as "oneight", I reverse the whole string and take the first reversed number
    # It's like evaluating the string from the right to the left and looking for reversed words (from "eight" to "thgie").
    # example: szcspm5sixtwovtrmvrthreefour7oneightqqj 
    # --> before I took "one" as last, now I take "eight"

    first = w2n.word_to_num(first)
    last = w2n.word_to_num(last[::-1])

    two_digits.append(int(str(first)+str(last)))
    sumup = sumup + two_digits[i]

print(sumup)

# %%
