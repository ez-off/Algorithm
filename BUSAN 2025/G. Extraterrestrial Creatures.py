'''
G. Extraterrestrial Creatures

There are N creatures with a number on its face.
If you touch an I-th creature, its number increases by A[I].
You will press the button on one with the smallest number, and if there is a tie, you choose the one with the smallest I.
Calculate the resulting numbers of each creatures after X touches.

Constraint: N <= 500000, X <= pow(10, 12)
'''

import sys


# 1. TO GET THE INPUT

alien_count, total_touch = map(int, sys.stdin.readline().split())

initial_val = list(map(int, sys.stdin.readline().split()))
added_val = list(map(int, sys.stdin.readline().split()))


# 2. BINARY SEARCH ON MINIMUM VALUE AFTER X TOUCHES

left = 0
right = pow(10, 20)

while left + 1 < right:
    
    min_val = (left + right) // 2
    
    touch = 0
    for idx in range(alien_count):
        if min_val <= initial_val[idx]:
            continue
        else:
            touch += (min_val - initial_val[idx]) // added_val[idx]
            if (min_val - initial_val[idx]) % added_val[idx] != 0:
                touch += 1
        
    if touch <= total_touch:
        left = min_val
    else:
        right = min_val

min_val = left


# 3. TO SOLVE THE PROBLEM

ans = initial_val[:]

left_touch = total_touch
for idx in range(alien_count):
    if left <= initial_val[idx]:
        continue
    else:
        now_touch = (min_val - initial_val[idx]) // added_val[idx]
        if (min_val - initial_val[idx]) % added_val[idx] != 0:
            now_touch += 1
        left_touch -= now_touch
        ans[idx] += added_val[idx] * now_touch

for idx in range(alien_count):
    if left_touch == 0:
        break
    if ans[idx] == min_val:
        ans[idx] += added_val[idx]
        left_touch -= 1

print(" ".join(map(str, ans)))