'''
D. Fibonacci Paths

You are given a graph with N vertices and M edges.
Count the number of distinct simple paths that forms a generalized Fibonacci sequence.

Constraint: N, M <= 200000
'''

import sys
MOD = 998244353


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    node_count, edge_count = map(int, sys.stdin.readline().split())
    value = list(map(int, sys.stdin.readline().split()))
    
    edges = []
    
    for edge in range(edge_count):
        nodeA, nodeB = map(int, sys.stdin.readline().split())
        nodeA -= 1
        nodeB -= 1
        edges.append((nodeA, nodeB))
    edges.sort(key = lambda x : value[x[1]])


    # 2. DP
    # Calculate the number of fibonacci paths that pass each edge.
    # dp[i][j] = The number of fibonacci paths that pass i with previous value j
    
    ans = 0
    dp = [{} for node in range(node_count)]
    
    for nodeA, nodeB in edges:
        
        count = 1
        
        last_val = value[nodeB] - value[nodeA]
        if last_val in dp[nodeA]:
            count = (count + dp[nodeA][last_val]) % MOD
        
        if value[nodeA] in dp[nodeB]:
            dp[nodeB][value[nodeA]] = (dp[nodeB][value[nodeA]] + count) % MOD
        else:
            dp[nodeB][value[nodeA]] = count
        
        ans = (ans + count) % MOD
    
    print(ans)