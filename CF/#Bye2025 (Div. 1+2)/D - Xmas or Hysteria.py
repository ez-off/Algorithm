'''
D. Xmas or Hysteria

There are N elves with distinct attack value A[i] and health value H[i].
The following process will repeat until it is impossible to do so.

(1) Choose a pair of distinct living elves X, Y such that elf X has not attacked before.
(2) Then, decrease A[X] by H[Y] and A[Y] by H[X]. A[X] and A[Y] remain unchanged.

Given an integer M, construct a valid sequence of attacks such that M elves are alive when the process ends.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    elf_count, goal_count = map(int, sys.stdin.readline().split())
    
    attack_val = list(map(int, sys.stdin.readline().split()))
    health_val = attack_val[:]
    
    
    # 2. TO SOLVE THE PROBLEM
    # Every survivor must have attacked, and every attack kills at least one. Thus, N >= 2 * M.
    
    if elf_count < 2 * goal_count:
        
        print(-1)
    
    else:
        
        arr = []
        for idx in range(elf_count):
            arr.append([health_val[idx], attack_val[idx], idx])
        arr.sort(reverse=True)
        
        ans = []
        
        if goal_count != 0:
            
            # Suicidal attack from the weakest
            
            while len(arr) > goal_count * 2:
                
                healthX, attackX, idxX = arr.pop()
                healthY, attackY, idxY = arr[-1]
                
                arr[-1][0] = healthY - attackX
                ans.append((idxX + 1, idxY + 1))

            # Attack from stronger half to weaker half
            
            for idx in range(goal_count):
                
                healthX, attackX, idxX = arr[idx]
                healthY, attackY, idxY = arr[-idx-1]
                
                ans.append((idxX + 1, idxY + 1))
            
            print(len(ans))
            for idxX, idxY in ans:
                print(idxX, idxY)
            
        else:
            
            # Attack to the strongest until the second strongest can kill the strongest
            # Suicidal attack if it is already possible
            
            for idx in range(elf_count-1, 0, -1):
                
                healthX, attackX, idxX = arr[idx]
                
                attack_first = True
                if arr[0][0] <= arr[1][1]:
                    attack_first = False
                
                if attack_first:
                    healthY, attackY, idxY = arr[0]
                    arr[0][0] = healthY - attackX
                else:
                    healthY, attackY, idxY = arr[idx-1]
                    arr[idx-1][0] = healthY - attackX
                ans.append((idxX + 1, idxY + 1))

            if arr[0][0] <= 0:
                print(len(ans))
                for idxX, idxY in ans:
                    print(idxX, idxY)
            else:
                print(-1)