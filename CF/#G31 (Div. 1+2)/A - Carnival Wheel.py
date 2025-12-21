'''
A - Carnival Wheel

You are given a number A.
After one spin, the number changes to (A + B) mod L.
You can spin any number of times.
Find the maximum number that can appear.

Constraint: L <= 5000
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    max_num, start_num, interval = map(int, sys.stdin.readline().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    # There is no need to check the same number twice.
    
    ans = start_num
    visited = [0 for num in range(max_num)]
    
    now_num = start_num
    while True:
        if visited[now_num]:
            break
        visited[now_num] = 1
        now_num = (now_num + interval) % max_num
        ans = max(ans, now_num)
    
    print(ans)