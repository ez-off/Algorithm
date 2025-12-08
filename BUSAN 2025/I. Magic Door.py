'''
I. Magic Door 

Simulate a gem game on M X N grid.
The game follows the following steps:

(1) Any match-3 groups of regular gems disappear.
(2) All gems above the vanished gems fall downward. Any bomb gem that moves down becomes activated.
(3) Repeat (1) and (2) until there is no match-3 groups left.
(4) All activated bombs explode simultaneously. Each bomb emits beams in horizontal and vertical directions until gold gem.
(5) All gems above the vanished gems fall downward. Any bomb gem that moves down becomes activated.
(6) Move back to Step 1.

Constraint: M, N <= 80
'''

import sys


# 2. FUNCTIONS TO SOLVE PROBLEM

# Step (1). Find match-3 groups and delete them

def match_three(grid):
    
    result = [[None for col in range(col_count)] for row in range(row_count)]
    
    for row in range(row_count):
        for col in range(col_count):
            
            if type(grid[row][col]) == int and 1 <= grid[row][col] <= 9:
                if row + 2 < row_count and grid[row][col] == grid[row+1][col] == grid[row+2][col]:
                    result[row][col], result[row+1][col], result[row+2][col] = "X", "X", "X"
                if col + 2 < col_count and grid[row][col] == grid[row][col+1] == grid[row][col+2]:
                    result[row][col], result[row][col+1], result[row][col+2] = "X", "X", "X"
    
    for row in range(row_count):
        for col in range(col_count):
            
            if result[row][col] != "X":
                result[row][col] = grid[row][col]
    
    return result

# Step (4). Explode the bomb

def explosion(grid):
    
    result = [[None for col in range(col_count)] for row in range(row_count)]
    
    for row in range(row_count):
        for col in range(col_count):
            
            if grid[row][col] == "A":
                for bomb_col in range(col, -1, -1):
                    if grid[row][bomb_col] == -1:
                        break
                    result[row][bomb_col] = "X"
                for bomb_col in range(col, col_count):
                    if grid[row][bomb_col] == -1:
                        break
                    result[row][bomb_col] = "X"
                for bomb_row in range(row, -1, -1):
                    if grid[bomb_row][col] == -1:
                        break
                    result[bomb_row][col] = "X"
                for bomb_row in range(row, row_count):
                    if grid[bomb_row][col] == -1:
                        break
                    result[bomb_row][col] = "X"
    
    for row in range(row_count):
        for col in range(col_count):
            if result[row][col] != "X":
                result[row][col] = grid[row][col]
    
    return result

# Step (2) & (5). Fall

def fall(grid):
    
    result = [[None for col in range(col_count)] for row in range(row_count)]
    
    for col in range(col_count):
        fall_count = 0
        for row in range(row_count-1, -1, -1):
            if grid[row][col] == "X":
                fall_count += 1
            else:
                if grid[row][col] == 0:
                    if fall_count == 0:
                        result[row+fall_count][col] = grid[row][col]
                    else:
                        result[row+fall_count][col] = "A"
                else:
                    result[row+fall_count][col] = grid[row][col]
    
    return result



# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = []
for row in range(row_count):
    grid.append(list(map(int, sys.stdin.readline().split())))

row1, col1, row2, col2 = map(int, sys.stdin.readline().split())
grid[row1-1][col1-1], grid[row2-1][col2-1] = grid[row2-1][col2-1], grid[row1-1][col1-1]


# 3. TO SOLVE THE PROBLEM

while True:
    
    phase1_done = True
    phase2_done = True
    
    # Phase 1

    while True:
        result = fall(match_three(grid))
        if grid == result:
            break
        phase1_done = False
        grid = result

    # Phase 2

    result = fall(explosion(grid))
    if grid != result:
        phase2_done = False
    grid = result
    
    if phase1_done and phase2_done:
        break

ans = 0

for row in range(row_count):
    for col in range(col_count):
        if grid[row][col] == None:
            ans += 1

print(ans)