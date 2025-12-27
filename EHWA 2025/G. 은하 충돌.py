'''
G. Galaxy Collision

There are N galaxies and M black holes.
They are connected by E directional edges without a cycle.

X-th black hole has a value V[X].
If you reach the X-th black hole, every distance decreases by V[X].
If a distance becomes 0, creatures living in two celestial bodies die.

Fortunately, you are invincible.
Determine if you can kill the given enemy by traveling space.

Constraint: N, M <= 200000, E <= 300000
'''

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

galaxy_count, hole_count, edge_count = map(int, sys.stdin.readline().split())
node_count = galaxy_count + hole_count + 1

OFFSET = hole_count

graph = [[] for node in range(node_count)]
in_degree = [0 for node in range(node_count)]

for edge in range(edge_count):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    graph[nodeB + OFFSET].append((nodeA + OFFSET, dist))
    in_degree[nodeA + OFFSET] += 1

hole_val = list(map(int, sys.stdin.readline().split()))

node_val = [0 for node in range(node_count)]
for hole in range(hole_count):
    node_val[OFFSET-hole-1] = hole_val[hole]

target = int(sys.stdin.readline())
target += OFFSET


# 2. TOPOLOGICAL SORT + DP
# Simple DFS from node 1 + OFFSET at original graph also works. 

max_val = [0 for node in range(node_count)]

queue = deque([])
for node in range(node_count):
    if in_degree[node] == 0:
        queue.append(node)
        if node < hole_count:
            max_val[node] = node_val[node]

while queue:
    now_node = queue.popleft()
    for next_node, dist in graph[now_node]:
        in_degree[next_node] -= 1
        max_val[next_node] = max(max_val[next_node], max_val[now_node])
        if in_degree[next_node] == 0:
            queue.append(next_node)
            if next_node < hole_count:
                max_val[next_node] += node_val[next_node]


# 3. TO SOLVE THE PROBLEM

val_to_kill = inf

for nodeA in range(node_count):
    for nodeB, dist in graph[nodeA]:
        if nodeA == target or nodeB == target:
            val_to_kill = min(val_to_kill, dist)

if val_to_kill <= max_val[1 + OFFSET]:
    print("HAPPY")
else:
    print("SAD")