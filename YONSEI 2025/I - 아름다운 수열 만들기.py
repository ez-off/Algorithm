'''
I. Beautiful Sequence Constructor

The sequence of length N is called 'beautiful' if it satisfies the following conditions.

- All elements are either 0, 1, or 2.
- All adjacent elements are distinct.
- Let D(X) be the sum of differences between X-elements and their adjacent elements. Then, D(0) = D(1) = D(2).

Given N, determine if it is possible to construct the beautiful sequence of length N.
If possible, print one.

Input : N <= 100000
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())

if length % 5 == 1:
    print("Yes")
    ans = []
    for repeat in range(length // 5):
        ans.append("0")
        ans.append("1")
    for repeat in range((length - 5) // 10 + 1):
        ans.append("0")
        ans.append("2")
    for repeat in range(length // 5):
        ans.append("1")
        ans.append("2")
    if length % 2 == 1:
        ans.append("0")
    print(" ".join(ans))
else:
    print("No")