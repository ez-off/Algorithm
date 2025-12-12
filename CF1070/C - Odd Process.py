'''
C. Odd Process

There are N coins, each of them with a value, and a natural number K.
You want to choose X coins to maximize total value.
However, every time the sum of the value becomes even, every coin you choose will disappear.
Find the maximum total value for all 1 <= X <= K.

Constraint: N <= 200000
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    total_value = sum(coins)
    
    
    # 2. SEPARATE ODD COINS AND EVEN COINS
    
    odds = []
    evens = []
    for coin in coins:
        if coin % 2 == 1:
            odds.append(coin)
        else:
            evens.append(coin)
    odds.sort(reverse=True)
    evens.sort(reverse=True)
    
    
    # 3. TO CONSTRUCT PREFIX SUM
    
    even_prefix_sum = [0]
    for num in evens:
        even_prefix_sum.append(even_prefix_sum[-1] + num)
    
    
    # 4. TO SOLVE THE PROBLEM
    # The optimal strategy is to choose the most valuable odd coin first, and to choose even coins from the most valuable one.
    
    odd_count = len(odds)
    even_count = len(evens)
    
    ans = [0 for coin_count in range(length + 1)]
    
    if even_count == 0:
        for coin_count in range(1, length + 1):
            if coin_count % 2 == 1:
                ans[coin_count] = odds[0]
            else:
                ans[coin_count] = 0
    elif odd_count == 0:
        pass
    else:
        for coin_count in range(length + 1):
            if coin_count <= 1 + even_count:
                ans[coin_count] = odds[0] + even_prefix_sum[coin_count - 1]
            else:
                if coin_count == length:
                    if total_value % 2 == 0:
                        ans[coin_count] = 0
                    else:
                        ans[coin_count] = ans[coin_count - 2]
                else:
                    ans[coin_count] = ans[coin_count - 2]
    
    print(" ".join(map(str, ans[1:])))