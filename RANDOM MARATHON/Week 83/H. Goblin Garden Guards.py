'''
H. Goblin Garden Guards

There are N points.
Given K circles, find the number of uncovered points.
'''

import sys


# 1. A FUNCTION TO DETERMINE IF POINT IS IN THE CIRCLE

def point_in_circle(x, y, center_x, center_y, r):
    
    if pow(x - center_x, 2) + pow(y - center_y, 2) <= pow(r, 2):
        return True
    else:
        return False


# 2. OTHER FUNCTIONS TO SOLVE THE PROBLEM

def hash(x, y):
    return x * 100000 + y

def erase(x, y):
    now_point = hash(x, y)
    if now_point in ans:
        ans[now_point] = 0


# 3. TO GET THE INPUT AND SOLVE THE PROBLEM

point_count = int(sys.stdin.readline())

ans = {}
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    now_point = hash(x, y)
    ans[now_point] = ans.get(now_point, 0) + 1 

circle_count = int(sys.stdin.readline())

for circle in range(circle_count):
    center_x, center_y, r = map(int, sys.stdin.readline().split())
    erase(center_x, center_y)
    for delta in range(1, r + 1):
        erase(center_x + delta, center_y)
        erase(center_x - delta, center_y)
        erase(center_x, center_y + delta)
        erase(center_x, center_y - delta)
    for x_delta in range(1, r + 1):
        for y_delta in range(1, r + 1):
            if point_in_circle(center_x + x_delta, center_y + y_delta, center_x, center_y, r):
                erase(center_x + x_delta, center_y + y_delta)
                erase(center_x + x_delta, center_y - y_delta)
                erase(center_x - x_delta, center_y + y_delta)
                erase(center_x - x_delta, center_y - y_delta)
            else:
                break

print(sum(ans.values()))