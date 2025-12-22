'''
E. Clean Arrangements

You want a linear arrangement of a rooted tree T that satisfies following conditions:

(1) T has no edge crossings except at common end vertices of edges.
(2) No edge covers the root vertex.

Given a rooted tree with the vertex 1 as a root, calculate the minimum possible sum of edges of the linear arrangement.

Constraint : N <= 5000 
'''

import sys
sys.setrecursionlimit(5001)


# 1. DFS FUNCTION 

def dfs(now_node):
    
    for connected_node in graph[now_node]:
        if parent[connected_node] == -1 and connected_node != 0:
            parent[connected_node] = now_node
            children[now_node].append(connected_node)
            dfs(connected_node)


# 3. TREE DP FUNCTION
# Observation 1. The number of left subtrees and right subtrees differ by at most 1.
# Observation 2. Subtrees with smaller size should come closer to the root node.

def tree_dp(now_node):
    
    subtrees_size = []
    for child_node in children[now_node]:
        tree_dp(child_node)
        size[now_node] += size[child_node]
        subtrees_size.append((size[child_node], child_node))
    subtrees_size.sort()
    
    sideA = 0
    sideB = 0
    for subtree_size, child_node in subtrees_size:
        if sideA < sideB:
            cost[now_node] += cost[child_node] + connect_cost[child_node] + sideA
            sideA += subtree_size
        else:
            cost[now_node] += cost[child_node] + connect_cost[child_node] + sideB
            sideB += subtree_size
    small_side, large_side = min(sideA, sideB), max(sideA, sideB)
    
    connect_cost[now_node] = small_side + 1


# 2. TO GET THE INPUT

node_count = int(sys.stdin.readline())

graph = [[] for node in range(node_count)]
for edge in range(node_count - 1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

parent = [-1 for node in range(node_count)]
children = [[] for node in range(node_count)]

dfs(0)


# 4. TO SOLVE THE PROBLEM
# cost[X] : The minimum cost to map the subtree rooted at node X
# connect_cost[X] : The minimum cost to connect the subtree rooted at node X to its parent

size = [1 for node in range(node_count)]

cost = [0 for node in range(node_count)]
connect_cost = [0 for node in range(node_count)]

tree_dp(0)

print(cost[0])