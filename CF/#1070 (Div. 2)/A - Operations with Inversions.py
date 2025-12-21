'''
A. Operations with Inversions

Given an array A of length N, you can choose pair of indices (X, Y) such that X < Y and A[X] > A[Y].
Then, the element at index Y will be removed.
Determine the maximum number of operations that can be performed.

Constraint: N <= 100
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    
    deleted = [0 for idx in range(length)]
    
    for i in range(length):
        for j in range(length):
            if i < j and arr[i] > arr[j]:
                deleted[j] = 1
    
    print(sum(deleted))