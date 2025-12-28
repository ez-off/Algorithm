'''
C. First or Second

There is an array A of which the length equals N.
An integer X is initially set to 0.
Santa will perform the following operation exactly N - 1 times.

(1) Choose the first or second element from array and remove it.
(2) If the first was chosen, add its value to X. Otherwise, subtract its value to X.

Determine the maximum possible value of X.
'''

import sys
inf = float('inf')


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    size = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. PREFIX SUM
    # front_point[idx] = The maximum point from A[:idx] when not using A[idx].
    # back_point[idx] = The maximum point from A[idx+1:] when not using A[idx].  
    
    front_point = [0 for idx in range(size)]
    for idx in range(1, size):
        if idx == 1:
            front_point[idx] = front_point[idx-1] + arr[idx-1]
        else:
            front_point[idx] = front_point[idx-1] + abs(arr[idx-1])
    
    back_point = [0 for idx in range(size)]
    for idx in range(size-2, -1, -1):
        back_point[idx] = back_point[idx+1] - arr[idx+1]
    
    ans = -inf
    for idx in range(size):
        ans = max(ans, front_point[idx] + back_point[idx])
    print(ans)