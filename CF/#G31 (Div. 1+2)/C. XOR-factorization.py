'''
C - XOR-factorization

Find an array A of K numbers such that XOR(A) = N, max(A) <= N, and sum(A) is maximized.

Constraint: K, N <= pow(10, 9)
'''

import sys


# 1. TO GET THE INPUT 

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    N, K = map(int, sys.stdin.readline().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    # For odd K, the answer is obvious.
    # For even K, it is optimal to have one 1-bit off for each number.
    
    ans = []
    
    if K % 2 == 0:
        
        binary_num = bin(N)[2:]
        
        one_loc = []
        one_before_zero = [0 for bit in range(len(binary_num))]
        
        # Count the number of 1-bits before each 0--bit
        
        now_one = 0
        for bit in range(len(binary_num)):
            if binary_num[bit] == "1":
                one_loc.append(bit)
                now_one += 1
            else:
                one_before_zero[bit] = now_one
        
        # If K is larger than the number of 1-bits, fill the rest with N        
        
        if K >= now_one:
            for repeat in range(K - now_one):
                ans.append(N)
            K = now_one
        
        # 
        
        for idx in range(len(one_loc)):
            
            loc = one_loc[idx]
            
            if K == 0:
                break
            
            now_num = []
            for bit in range(len(binary_num)):
                if binary_num[bit] == "0":
                    if loc < bit:
                        if one_before_zero[bit] % 2 == 1 and idx == one_before_zero[bit] - 1:
                            now_num.append("0")
                        else:
                            now_num.append("1")
                    else:
                        now_num.append("0")
                else:
                    if K == 1:
                        if loc <= bit:
                            now_num.append("0")
                        else:
                            now_num.append("1")
                    else:
                        if loc == bit:
                            now_num.append("0")
                        else:
                            now_num.append("1")
            ans.append(int("".join(now_num), 2))
            
            K -= 1
            
    else:
        
        for repeat in range(K):
            ans.append(N)
    
    print(" ".join(map(str, ans)))