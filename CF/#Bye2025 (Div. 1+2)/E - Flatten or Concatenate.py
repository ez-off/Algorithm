'''
E. Flatten or Concatenate

There are two arrays A and B.
Initially, both of them consist of a single integer pow(2, K).

Your friend applied the following two types of operations any times in any order:
(1) Flatten - Choose either A or B, and select any maximal element X and replace it with two copies of X / 2.
(2) Concatenate - Set both A and B to A + B.

Find the maximum element of A when only given the length of A.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())

    
    # 2. TO SOLVE THE PROBLEM
    # Find a point that divides the sum by 2, and move to the shorter segment.
    
    print("?", 1, length)
    sys.stdout.flush()
    total_sum = int(sys.stdin.readline())
    
    interval_sum = total_sum
    interval_left = 1
    interval_right = length
    
    while interval_left != interval_right:
        
        now_left = interval_left
        now_right = interval_right
        
        while now_left + 1 < now_right:
            
            now_mid = (now_left + now_right) // 2
            
            print("?", interval_left, now_mid)
            sys.stdout.flush()
            result = int(sys.stdin.readline())
            if result <= interval_sum // 2:
                now_left = now_mid
                if result == interval_sum // 2:
                    break
            else:
                now_right = now_mid
        
        if now_left - interval_left < interval_right - now_left:
            interval_right = now_left
        else:
            interval_left = now_left + 1
        interval_sum //= 2
    
    print("?", interval_left, interval_right)
    sys.stdout.flush()
    ans = int(sys.stdin.readline())
    print("!", ans)
    sys.stdout.flush()