import sys
from math import atan


# 2. FUNCTIONS TO SOLVE THE PROBLEM

# CCW

def ccw(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    res = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    if res < 0:
        return -1
    elif res > 0:
        return 1
    else:
        return 0

# Angular Sort

def get_angle(point):
    
    x, y = point
    
    if x >= x0 and y > y0:
        return (1, atan((x - x0) / (y - y0)))
    elif x > x0 and y <= y0:
        return (2, atan((y0 - y) / (x - x0)))
    elif x <= x0 and y < y0:
        return (3, atan((x0 - x) / (y0 - y)))
    else:
        return (4, atan((y - y0) / (x0 - x)))
    

# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))


# 3. TO SOLVE THE PROBLEM

ans = [0 for k in range(point_count - 1)]

for idx in range(point_count):

    # Fix a point p0 and sort the others by angle (Clockwise)
    
    p0 = points[idx]
    x0, y0 = p0
    
    left_points = points[:idx] + points[idx+1:]
    left_points.sort(key=get_angle)
    
    # Fix a half-linear axis that starts from p0 and passes p1
    
    j = 0
    k = 0
    
    for i in range(point_count - 1):
        
        p1 = left_points[i]
        x1, y1 = p1
        
        # Find a point with the largest angle within 180° (Clockwise)
        
        if j < i:
            j = i
        while (j + 1) % len(left_points) != i and ccw(p0, p1, left_points[(j + 1) % len(left_points)]) < 0:
            j += 1
            
        p_max = left_points[j % len(left_points)]
        x_max, y_max = p_max
        
        # Get a point of which angle equals 90° (Clockwise)
        
        p_right = (x0 - y0 + y1, x0 + y0 - x1)
        x_right, y_right = p_right
        
        # To get all possible K
        
        if ccw(p0, p_right, p_max) < 0:
            
            if k < i:
                k = i
            while k % len(left_points) != j and ccw(p0, p_right, left_points[k % len(left_points)]) > 0:
                k += 1
            
            ans[k % len(left_points) - i - 1] += 1
            ans[j % len(left_points) - i] -= 1
            
# Difference Array

for k in range(1, point_count-1):
    ans[k] += ans[k-1]

for k in range(point_count-2):
    print(ans[k] * 2)