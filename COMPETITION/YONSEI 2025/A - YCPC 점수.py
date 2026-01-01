'''
A. YCPC Score

You are given numbers of 'Y', 'C', and 'P' you can use.
Calculate the maximum number of 'YCPC' you can make.

Input : max(Y, C, P) <= pow(10, 6)
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

y_count, c_count, p_count = map(int, sys.stdin.readline().split())

print(min(y_count, c_count // 2, p_count))