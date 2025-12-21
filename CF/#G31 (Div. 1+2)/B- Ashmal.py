'''
B - Ashmal

You are given an array A of N strings, and an empty string S.
In the X-th step, you should add A[X] to the either beginning or end of S.
Find the lexicographically smallest S after N steps.

Constraint: N <= 1000, sum(|A[X]|) <= 4000
'''

import sys
from collections import deque
from copy import deepcopy


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    word_count = int(sys.stdin.readline())
    words = list(sys.stdin.readline().strip().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = deque([])
    
    for idx in range(word_count):
        
        case_front = deepcopy(ans)
        case_front.appendleft(words[idx])
        
        case_back = deepcopy(ans)
        case_back.append(words[idx])

        if "".join(list(case_front)) < "".join(list(case_back)):
            ans.appendleft(words[idx])
        else:
            ans.append(words[idx]) 
    
    ans = "".join(list(ans))
    print(ans)