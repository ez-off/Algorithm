'''
F. Binary Search

You want to do binary search on an interval [0, L] by following steps:

(1) For an interval [S, E], search M = floor((S + E) / 2). If a person at M is binary, stop the search.
(2) Check an interval with more binary people between [S, M-1] and [M+1, E].

Locate N binary people so that the number of search becomes maximum.

Constraint: N <= pow(10, 5), L <= pow(10, 18)
'''


import sys


# 1. D&C FUNCTION FOR BINARY SEARCH

def solve(left, right, now_people):
    
    if now_people != 0:
        
        if right - left + 1 == now_people:
            
            for loc in range(left, right + 1):
                ans.append(loc)
        
        else:
            
            mid = (left + right) // 2
            
            solve(left, mid - 1, now_people // 2)
            solve(mid + 1, right, now_people - now_people // 2)


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

people_count, length = map(int, sys.stdin.readline().split())

ans = []
solve(0, length, people_count)
print(" ".join(map(str, ans)))