'''
B. Impost or Sus

A string R consisting only of "s" and "w" is called suspicious iff all of the following conditions hold:

(1) The letter "s" appears at least twice.
(2) For every "u", the two nearest occurrences of "s" are the same number of characters away from the "u".

You can choose an index I and set R[i] to "s" any number of time.
Determine the minimum number of operations needed to make R suspicious.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    word = list(sys.stdin.readline().strip())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = 0
    
    s_idx = True
    for idx in range(len(word)):
        
        # The first and the last character must be "s".
        if idx == 0 or idx == len(word) - 1:
            s_idx = True
        
        # "u" must be surrounded by "s".
        if s_idx:
            if word[idx] == "u":
                ans += 1
            s_idx = False
        else:
            if word[idx] == "u":
                s_idx = True
    
    print(ans)