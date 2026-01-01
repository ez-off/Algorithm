'''
D. Combining Chocolate

There are N chocolates.
If two chocolates have the same height, you can combine them.
Calculate the maximum possible area of a chocolate you can make.

Constraint: N <= 200000
'''

import sys


# 1. TO GET THE INPUT

chocolate_count = int(sys.stdin.readline())

heights = list(map(int, sys.stdin.readline().split()))
widths = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

chocolates = []
for idx in range(chocolate_count):
    chocolates.append((heights[idx], widths[idx]))
chocolates.sort(reverse=True)

ans = 0
now_width = 0
for height, width in chocolates:
    now_width += width
    ans = max(ans, height * now_width)
print(ans)