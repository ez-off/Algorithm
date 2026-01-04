'''
G. Assemble Toy

You want to make a toy with N parts.
Some of them are basic parts which does not require assembly.
Some of them are intermediate parts which can be made by assembly.
Given assembly method for each part, determine how many each basic parts are needed.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

part_count = int(sys.stdin.readline())
edge_count = int(sys.stdin.readline())

graph = [[] for part in range(part_count)]
in_degree = [0 for part in range(part_count)]
out_degree = [0 for part in range(part_count)]

for edge in range(edge_count):
    partA, partB, count = map(int, sys.stdin.readline().split())
    partA -= 1
    partB -= 1
    graph[partA].append((partB, count))
    in_degree[partB] += 1
    out_degree[partA] += 1


# 2. TOPOLOGICAL SORT

ans = [0 for part in range(part_count)]
ans[-1] = 1

queue = deque([])
for part in range(part_count):
    if in_degree[part] == 0:
        queue.append(part)

while queue:
    now_part = queue.popleft()
    for next_part, count in graph[now_part]:
        ans[next_part] += ans[now_part] * count
        in_degree[next_part] -= 1
        if in_degree[next_part] == 0:
            queue.append(next_part)


# 3. TO SOLVE THE PROBLEM

for part in range(part_count):
    if out_degree[part] == 0:
        print(part + 1, ans[part])