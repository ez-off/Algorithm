'''
A. Good Grass

You are given R X C grid.
Find 3 X 3 sub-grid of which sum is the greatest.
'''

import sys
inf = float('inf')


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = []
for row in range(row_count):
    grid.append(list(map(int, sys.stdin.readline().split())))


# 2. TO SOLVE THE PROBLEM - BRUTE-FORCING

ans_row = inf
ans_col = inf
ans_val = 0

for row in range(row_count-2):
    for col in range(col_count-2):
        
        val = 0
        for now_row in range(row, row+3):
            for now_col in range(col, col+3):
                val += grid[now_row][now_col]
        
        if val > ans_val or (val == ans_val and (row, col) < (ans_row, ans_col)):
            ans_row = row
            ans_col = col
            ans_val = val

print(ans_val)
print(ans_row + 1, ans_col + 1)