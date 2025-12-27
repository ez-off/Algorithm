'''
E. This way to Ehwa?

There are N nodes. 
From node X, you can only go to node A[X].
For all node, calculate the minimum number of steps to node N. 

Constraint: N <= 200000
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())
destination = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# Reverse the graph, then BFS from node N would work.

graph = {}
for node in range(node_count):
    graph[node] = []
for node in range(node_count):
    graph[destination[node] - 1].append(node)

visited = [-1 for node in range(node_count)]
visited[node_count-1] = 0

queue = deque([node_count-1])
while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if visited[next_node] == -1:
            visited[next_node] = visited[now_node] + 1
            queue.append(next_node)

for node in range(node_count):
    print(visited[node])