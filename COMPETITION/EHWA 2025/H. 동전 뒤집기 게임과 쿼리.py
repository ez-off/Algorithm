'''
H. Coin-flip Game and Query

Two women - X and Y - are playing coin-flip game with N coins.
The rules are following.

(1) X can choose a maximum contiguous substring of head and flip them all. If it is impossible, she does nothing.
(2) Y can choose a maximum contiguous substring of tail and flip them all. If it is impossible, she does nothing.
(3) People who flip all coins at once wins.

Another woman Z was intrigued by the game and decides to ask Q queries.
Answer following two types of queries.

(1) Flip the I-th coin.
(2) Determine who will win using L-th coin to R-th coin.

Constraint: N <= 500000
'''

import sys


# 3. FUNCTIONS FOR SEGMENT TREE

def change(idx, val):
    
    now_node = idx + OFFSET
    
    seg_tree[now_node] = val
    now_node >>= 1
    
    while now_node != 0:
        seg_tree[now_node] = seg_tree[now_node << 1] + seg_tree[(now_node << 1) | 1]
        now_node >>= 1

def partial_sum(idx_left, idx_right):
    
    node_left = idx_left + OFFSET
    node_right = idx_right + OFFSET
    
    result = 0
    while node_left <= node_right:
        if node_left % 2 == 1:
            result += seg_tree[node_left]
            node_left += 1
        if node_right % 2 == 0:
            result += seg_tree[node_right]
            node_right -= 1
        node_left >>= 1
        node_right >>= 1
    
    return result


# 1. TO GET THE INPUT

coin_count = int(sys.stdin.readline())
coins = list(sys.stdin.readline().strip())


# 2. TO CREATE A SEGMENT TREE

OFFSET = 1 << 19

node_count = 1 << 20
seg_tree = [0 for node in range(node_count)]
for idx in range(coin_count - 1):
    if coins[idx] != coins[idx+1]:
        now_node = idx + OFFSET
        while now_node != 0:
            seg_tree[now_node] += 1
            now_node >>= 1


# 4. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query_num in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    if len(query) == 2:
        
        query_type, idx = query
        idx -= 1
        
        if coins[idx] == "H":
            coins[idx] = "T"
        else:
            coins[idx] = "H"
        
        if idx != 0:
            if coins[idx-1] != coins[idx]:
                change(idx-1, 1)
            else:
                change(idx-1, 0)
        if idx != coin_count - 1:
            if coins[idx+1] != coins[idx]:
                change(idx, 1)
            else:
                change(idx, 0)

    else:
        
        query_type, idxA, idxB = query
        idxA -= 1
        idxB -= 1
        
        result = partial_sum(idxA, idxB - 1)
        if coins[idxA] == "H":
            if result % 4 != 1:
                print("First")
            else:
                print("Second")
        else:
            if result % 4 == 3:
                print("First")
            else:
                print("Second")