'''
C. Bay

There is a spanning tree T of a grid of size N X N.
You add an edge, and then, the region enclosed is created.
Your goal is to make the region such that the area equals to S.
Find all edges that creates enclosed region of area S.

Constraint: N <= 300
'''


import sys
inf = float('inf')


# 3. DFS-BASED FUNCTIONS FOR TREE DP

def dfs(now_cell):
    
    for connected_cell in cell_graph[now_cell]:
        if parent[connected_cell] == inf:
            parent[connected_cell] = now_cell
            children[now_cell].append(connected_cell)
            dfs(connected_cell)

def count_size(now_cell):
    
    for child in children[now_cell]:
        subtree_size[now_cell] += count_size(child)
    
    return subtree_size[now_cell]


# 1. TO GET THE INPUT

size, goal_area = map(int, sys.stdin.readline().split())

point_graph = [set() for point in range(size * size)]
for edge in range(size * size - 1):
    pointA, pointB = map(int, sys.stdin.readline().split())
    pointA -= 1
    pointB -= 1
    point_graph[pointA].add(pointB)
    point_graph[pointB].add(pointA)


# 2. TO CREATE CELL GRAPH 

horizontal_root_cells = set()
vertical_root_cells = set()

cell_graph = [[] for cell in range((size - 1) * (size - 1))]

# Horizontal lines

for y in range(size):
    for x in range(size-1):
        point = y * size + x
        if point + 1 not in point_graph[point]:
            if y == 0:
                vertical_root_cells.add(y * (size - 1) + x)
            elif y == size - 1:
                vertical_root_cells.add((y - 1) * (size - 1) + x)
            else:
                cellA = (y - 1) * (size - 1) + x
                cellB = y * (size - 1) + x
                cell_graph[cellA].append(cellB)
                cell_graph[cellB].append(cellA)

# Vertical lines

for y in range(size-1):
    for x in range(size):
        point = y * size + x
        if point + size not in point_graph[point]:
            if x == 0:
                horizontal_root_cells.add(y * (size - 1) + x)
            elif x == size - 1:
                horizontal_root_cells.add(y * (size - 1) + x - 1)
            else:
                cellA = y * (size - 1) + x
                cellB = y * (size - 1) + x - 1
                cell_graph[cellA].append(cellB)
                cell_graph[cellB].append(cellA)


# 4. TO CONSTRUCT A FOREST

parent = [inf for cell in range((size - 1) * (size - 1))]
children = [[] for cell in range((size - 1) * (size - 1))]

for cell in horizontal_root_cells:
    parent[cell] = -1
    dfs(cell)
for cell in vertical_root_cells:
    parent[cell] = -1
    dfs(cell)


# 5. TO COUNT THE SIZE OF SUBTREE FOR EACH NODE
# The area when cutting the edge between a cell and its parent equals to the size of the subtree rooted at that cell.

subtree_size = [1 for cell in range((size - 1) * (size - 1))]

for root in horizontal_root_cells:
    count_size(root)
for root in vertical_root_cells:
    count_size(root)


# 6. TO SOLVE THE PROBLEM

ans_count = 0
ans_arr = []

for cell in range((size - 1) * (size - 1)):
    if subtree_size[cell] == goal_area:
        
        ans_count += 1
        
        y = cell // (size - 1)
        x = cell % (size - 1)
        point = y * size + x
        
        if cell in horizontal_root_cells:
            if x == 0:
                ans_arr.append((point, point + size))
            else:
                ans_arr.append((point + 1, point + size + 1))
        elif cell in vertical_root_cells:
            if y == 0:
                ans_arr.append((point, point + 1))
            else:
                ans_arr.append((point + size, point + size + 1))
        else:
            if parent[cell] == cell - size + 1:
                ans_arr.append((point, point + 1))
            elif parent[cell] == cell - 1:
                ans_arr.append((point, point + size))
            elif parent[cell] == cell + 1:
                ans_arr.append((point + 1, point + size + 1))
            else:
                ans_arr.append((point + size, point + size + 1))

ans_arr.sort()

if ans_count == 0:
    print(0)
    print(0, 0)
else:
    ans_pointA, ans_pointB = ans_arr[0]
    print(ans_count)
    print(ans_pointA + 1, ans_pointB + 1)
