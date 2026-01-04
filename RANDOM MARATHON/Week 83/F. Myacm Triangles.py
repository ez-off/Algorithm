'''
F. Myacm Triangles

Given N points, find the maximum area of triangle which does not contains other points.
'''

import sys


# 2. FUNCTIONS TO SOLVE THE PROBLEM

def ccw(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    result = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    
    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0

def point_on_line(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    if ccw(p1, p2, p3) == 0 and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
        return True
    else:
        return False

def point_in_triangle(p1, p2, p3, p4):
    
    if ccw(p1, p2, p4) == ccw(p2, p3, p4) == ccw(p3, p1, p4):
        return True
    elif point_on_line(p1, p2, p4) or point_on_line(p2, p3, p4) or point_on_line(p3, p1, p4):
        return True
    else:
        return False

def area(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    result = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    return abs(result) / 2


# 1. TO GET THE INPUT

while True:
    
    point_count = int(sys.stdin.readline())
    if point_count == 0:
        break

    points = []
    for point in range(point_count):
        label, x, y = sys.stdin.readline().strip().split()
        x = int(x)
        y = int(y)
        points.append((x, y, label))


    # 3. TO SOLVE THE PROBLEM

    ans = ""
    max_area = 0

    for i in range(point_count):
        for j in range(i+1, point_count):
            for k in range(j+1, point_count):
                
                x1, y1, label1 = points[i]
                p1 = (x1, y1)
                x2, y2, label2 = points[j]
                p2 = (x2, y2)
                x3, y3, label3 = points[k]
                p3 = (x3, y3)
                
                possible = True
                for x in range(point_count):
                    if x != i and x != j and x != k:
                        x4, y4, label4 = points[x]
                        p4 = (x4, y4)
                        if point_in_triangle(p1, p2, p3, p4):
                            possible = False
                            break
                
                if possible:
                    now_area = area(p1, p2, p3)
                    if now_area > max_area:
                        ans = label1 + label2 + label3
                        max_area = now_area

    print(ans)