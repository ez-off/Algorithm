'''
G. Multi-Factorial

Process Q queries: Given N and K, calculate K-multi factorial of N.

Input : Q, N, K <= 100000
'''

import sys
MOD = 998244353


# 1. PREPROCESSING (K <= 300)

factorial = [[1 for last_num in range(100001)] for interval in range(301)]

for interval in range(1, 301):
    for last_num in range(1, 100001):
        if last_num < interval:
            factorial[interval][last_num] = last_num
        else:
            factorial[interval][last_num] = (factorial[interval][last_num - interval] * last_num) % MOD


# 2. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    N, K = map(int, sys.stdin.readline().split())
    
    if K <= 300:
        print(factorial[K][N])
    else:
        num = N
        ans = N
        while num - K > 0:
            num -= K
            ans = (ans * num) % MOD
        print(ans)