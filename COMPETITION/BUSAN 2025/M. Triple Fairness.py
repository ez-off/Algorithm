'''
M. Triple Fairness

Each competitive programming team consists of three members.
There are 3N problems: difficulty of 1 ~ N, 3 problems for each difficulty.
The members can divide problems either sequentially or by using remainders.
Make sure that each member must be assigned exactly one problem for each difficulty from 1 to N regardless of the method.

Constraint: N <= 200
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# This works because N is not a multiple of 3.

max_level = int(sys.stdin.readline())

ans = [level for level in range(1, max_level + 1)] * 3
print(" ".join(map(str, ans)))