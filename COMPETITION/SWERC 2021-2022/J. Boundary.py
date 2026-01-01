'''
J. Boundary

You want to fill the boundary of W * L bathroom with 1 * A tiles.
Print all possible A.

Input : W, L <= pow(10, 9)
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    width, length = map(int, sys.stdin.readline().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    # 1 and 2 are always possible.
    # Make sure not to miss 2 at the loop as we need to check not only 2 but also, for example, width / 2.
    
    ans = set([1, 2])
    
    for num in range(1, 100000):
        if width % num == 0:
            if (length - 2) % num == 0:
                ans.add(num)
            if (length - 2) % (width // num) == 0:
                ans.add(width // num)
        if (width - 1) % num == 0:
            if (length - 1) % num == 0:
                ans.add(num)
            if (length - 1) % ((width - 1) // num) == 0:
                ans.add((width - 1) // num)
        if (width - 2) % num == 0:
            if length % num == 0:
                ans.add(num)
            if length % ((width - 2) // num) == 0:
                ans.add((width - 2) // num)

    ans = sorted(ans)
    print(len(ans), " ".join(map(str, ans)))