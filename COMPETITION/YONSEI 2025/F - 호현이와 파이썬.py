'''
F. Hohyun and Python

You want to check if N variables are all distinct.
However, you can only write one line in Python and the only operator you can use is !=.
Determine the minimum number of != needed.

Input : N <= 200000
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# The problem is equivalent to find Euler trail on complete graph.

num = int(sys.stdin.readline())

if num % 2 == 1:
    print(num * (num - 1) // 2)
else:
    print(num * (num - 1) // 2 + num // 2 - 1)