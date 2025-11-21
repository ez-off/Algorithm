'''
F. Bottle Arrangements

There are N wines arranged in a line and M critics.
Each critic will sip only from a contiguous interval of bottles.
I-th critic wants to taste exactly R[i] red wines and W[i] red wines.
Find an arrangement that satisfies all the requests.
If impossible, state that no such arrangement exists.

Input : N, M, max(R), max(W) <= 100
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    wine_count, critic_count = map(int, sys.stdin.readline().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    # The idea is to arrange all red wines, then all white wines.
    
    red_max = 0
    white_max = 0
    
    for critic in range(critic_count):
        red_count, white_count = map(int, sys.stdin.readline().split())
        red_max = max(red_max, red_count)
        white_max = max(white_max, white_count)
    
    if red_max + white_max > wine_count:
        print("IMPOSSIBLE")
    else:
        left_count = wine_count - (red_max + white_max)
        print("R" * (red_max + left_count) + "W" * white_max)