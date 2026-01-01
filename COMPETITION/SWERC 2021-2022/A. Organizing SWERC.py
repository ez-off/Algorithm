'''
A. Organizing SWERC

You are given N problems, each with a beauty value and a difficulty. 
Select exactly one problem for each difficulty level such that the total beauty is maximized. 
If it is not possible, output "MORE PROBLEMS".

Input : N <= 100
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    ans = [0 for difficulty in range(10)]
    
    problem_count = int(sys.stdin.readline())
    for problem in range(problem_count):
        beauty, difficulty = map(int, sys.stdin.readline().split())
        difficulty -= 1
        ans[difficulty] = max(ans[difficulty], beauty)
    
    if 0 in ans:
        print("MOREPROBLEMS")
    else:
        print(sum(ans))