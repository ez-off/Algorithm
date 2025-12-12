'''
B. Optimal Shifts

You are given a binary string S of length N containing at least one 1.
Your goal is to obtain a binary string of same length, consisting only of 1s.
You can perform the following operation any number of times:

Let S' be a cyclic right shift of the string S by D. 
You can obtain S | S' with D coins.

Determine the minimum number of coins needed.

Constraint: N <= 200000
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    string = sys.stdin.readline().strip()
    
    
    # 2. TO SOLVE THE PROBLEM
    # What matters is the farthest distance of 0 from 1. 
    
    first_one_idx = string.find("1")
    
    now_idx = (first_one_idx + 1) % length
    latest_one_idx = first_one_idx
    
    ans = 0
    
    while True:
        
        if string[now_idx] == "1":
            
            zero_length = now_idx - latest_one_idx - 1
            if zero_length < 0:
                zero_length += length
            ans = max(ans, zero_length)
            
            latest_one_idx = now_idx
        
        now_idx = (now_idx + 1) % length
        if now_idx == (first_one_idx + 1) % length:
            break
    
    print(ans)