'''
H. MED MAX

There is an array A with N distinct positive integers.
Calculate the maximum value of MED(B) + MEX(B) where B is a non-empty subsequence of A.

Input : N <= 200000, max(A) <= pow(10, 9)
'''

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


# 2. TO CALCULATE THE MAXIMUM MEX VALUE

now_mex = 0

mex_elements = []
larger_elements = []

for idx in range(length):
    if arr[idx] < now_mex:
        continue
    elif arr[idx] == now_mex:
        mex_elements.append(arr[idx])
        now_mex += 1
    else:
        larger_elements.append(arr[idx])


# 3. TO SOLVE THE PROBLEM
# If len(mex_elements) < len(larger_elements), it is better to choose some elements from larger_elements to maximize median value.
# Otherwise, it is better to put all elements from larger_elements.

ans = arr[-1]

for idx in range(len(mex_elements) - 1, -1, -1):
    now_mex = mex_elements[idx] + 1
    if idx < len(larger_elements):
        ans = max(ans, now_mex + larger_elements[-idx-1])
    else:
        key_idx = (len(mex_elements) + len(larger_elements)) // 2
        ans = max(ans, now_mex + mex_elements[key_idx])

print(ans)