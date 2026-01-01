'''
C. Find Point

You are given two points A = (x1, y1) and B = (x2, y2).
Find the point C = (x, y) such that the taxi distance from A to C is equal to the taxi distance from B to C.

Input : -pow(10, 9) <= x1, x2, y1, y2 <= pow(10, 9)
'''

import sys


# 1. TO GET THE INPUT

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())

if x1 > x2 or (x1 == x2 and y1 > y2):
    x1, y1, x2, y2 = x2, y2, x1, y1


# 2. TO SOLVE THE PROBLEM

total_dist = abs(x1 - x2) + abs(y1 - y2)

if total_dist % 2 == 0:
    if x2 - x1 >= total_dist // 2:
        print(x1 + total_dist // 2, y1)
    else:
        if y1 > y2:
            print(x2, y1 - total_dist // 2 + (x2 - x1))
        else:
            print(x2, y1 + total_dist // 2 - (x2 - x1))
else:
    print(-1)