'''
D. Obstacle on the Right

N cars will enter an intersection. 
X-th car will enter at T[X] from direction D[X].
A car can pass through the intersection if there is no car at right direction.
Determine when each car can pass through the intersection.
'''

import sys
from collections import deque


# 2. A FUNCTION TO CLEAR INTERSECTION

def clear(interval):
    
    for seconds in range(interval):
        
        can_escape = [0 for direction in range(4)]
        for direction in range(4):
            if len(intersection[direction]) != 0 and len(intersection[(direction+3) % 4]) == 0:
                can_escape[direction] = 1

        if sum(can_escape) == 0:
            break
        
        for direction in range(4):
            if can_escape[direction]:
                escape_driver = intersection[direction].popleft()
                ans[escape_driver] = now_time + seconds


# 1. TO GET THE INPUT

driver_count = int(sys.stdin.readline())

drivers = []
for driver in range(driver_count):
    entry_time, entry_direction = sys.stdin.readline().strip().split()
    entry_time = int(entry_time)
    drivers.append((entry_time, entry_direction, driver))


# 3. TO SOLVE THE PROBLEM

direction_to_num = {"U":0, "R":1, "D":2, "L":3}

ans = [-1 for driver in range(driver_count)]

intersection = [deque() for direction in range(4)]

now_time = None
for entry_time, entry_direction, entry_driver in drivers:
    if now_time != None and now_time != entry_time:
        clear(min(driver_count, entry_time - now_time))
    intersection[direction_to_num[entry_direction]].append(entry_driver)
    now_time = entry_time
clear(driver_count)

for escape_time in ans:
    print(escape_time)