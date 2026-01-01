'''
L. Circular Maze

Given a circular maze with N walls, determine if it can be solved.

Input : N <= 5000
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    wall_count = int(sys.stdin.readline())
    
    
    # 2. TO CONSTRUCT GRID
    
    grid = [[0 for angle in range(720)] for radius in range(42)]
    
    for wall in range(wall_count):
        
        wall_info = sys.stdin.readline().strip().split()
        
        if wall_info[0] == "C":
            
            radius, start_angle, end_angle = map(int, wall_info[1:])
            
            now_angle = start_angle * 2
            while now_angle != end_angle * 2:
                grid[radius * 2][now_angle] = 1
                now_angle = (now_angle + 1) % 720
            
        else:
            
            start_radius, end_radius, angle = map(int, wall_info[1:])
            
            for radius in range(start_radius * 2, end_radius * 2 + 1):
                grid[radius][angle * 2] = 1
    
    
    # 3. BFS
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    visited = [[0 for angle in range(720)] for radius in range(42)]
    
    queue = deque([])
    for angle in range(720):
        queue.append((0, angle))
        visited[0][angle] = 1
    
    while queue:
        now_radius, now_angle = queue.popleft()
        for idx in range(4):
            next_radius = now_radius + dy[idx]
            next_angle = (now_angle + dx[idx]) % 720
            if 0 <= next_radius < 42 and 0 <= next_angle < 720 and grid[next_radius][next_angle] == 0 and visited[next_radius][next_angle] == 0:
                visited[next_radius][next_angle] = 1
                queue.append((next_radius, next_angle))
    
    
    # 4. TO SOLVE THE PROBLEM
    
    if visited[41][0]:
        print("YES")
    else:
        print("NO")