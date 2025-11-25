'''
B. Drone Photo

There are N X N students, whose ages are all distinct from 1 to pow(N, 2).

You want to choose four students on the vertices of an axis-aligned rectangle.
Then, you will have two younger students hold one of the poles and the two older students hold the other pole.
Determine the number of cases such that two poles are parallel and do not cross.

Input : N <= 1500
'''

import sys


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

ages = []
for row in range(size):
    ages.append(list(map(int, sys.stdin.readline().split())))


# 2. TO CALCULATE THE NUMBER OF YOUNGER CONTESTANTS IN THE SAME ROW AND THE SAME COLUMN

age_loc = [(0, 0) for age in range(size ** 2 + 1)]
for row in range(size):
    for col in range(size):
        age_loc[ages[row][col]] = (row, col)

row_checked = [0 for row in range(size)]
col_checked = [0 for col in range(size)]

row_younger_count = [0 for age in range(size ** 2 + 1)]
col_younger_count = [0 for age in range(size ** 2 + 1)]

for age in range(1, size ** 2 + 1):
    row, col = age_loc[age]
    row_younger_count[age] = row_checked[row]
    col_younger_count[age] = col_checked[col]
    row_checked[row] += 1
    col_checked[col] += 1


# 3. TO SOLVE THE PROBLEM

# Let us define a point of rectangle intermediate if exactly one of the two adjacent points is younger.
# Observation 1. Rectangles can have either two intermediate points or none.
# Observation 2. Valid rectangles must have two intermediate points.

# Let row_younger_count[age] be RYC(A) and col_younger_count[age] be CYC(A).
# Then, the answer is sum(RYC(A) * (N - 1 - CYC(A)) + (N - 1 - RYC(A)) * CYC(A)) // 2.
# This is because it counts all cases where A is an intermediate point.

ans = 0
for age in range(1, size ** 2 + 1):
    ans += row_younger_count[age] * (size - 1 - col_younger_count[age]) + (size - 1 - row_younger_count[age]) * col_younger_count[age]
ans //= 2

print(ans)