'''
L. Segments

You are given N segments parallel to the X-axis.
Answer Q queries: Given a vertical line, determine the maximum extension length between all segments to meet the line.

Constraint: N, Q <= 200000
'''

import sys
inf = float('inf')


# 1. TO GET THE INPUT

line_count, query_count = map(int, sys.stdin.readline().split())

lines = []

for line in range(line_count):
    left, right, y_coordinate = map(int, sys.stdin.readline().split())
    lines.append((left, right))


# 2. TO SOLVE THE PROBLEM
# The only two points we need are the rightmost left point and the leftmost right point.

rightmost_left = -inf
leftmost_right = inf

for left, right in lines:
    rightmost_left = max(rightmost_left, left)
    leftmost_right = min(leftmost_right, right)

for query in range(query_count):
    x_coordinate = int(sys.stdin.readline())
    # Be careful when all segments have overlapping interval.
    if rightmost_left <= leftmost_right:
        if x_coordinate <= rightmost_left:
            print(rightmost_left - x_coordinate)
        elif rightmost_left <= x_coordinate < leftmost_right:
            print(0)
        else:
            print(x_coordinate - leftmost_right)
    else:
        print(max(abs(x_coordinate - rightmost_left), abs(x_coordinate - leftmost_right)))