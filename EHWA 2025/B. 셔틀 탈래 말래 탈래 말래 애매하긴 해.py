'''
B. Shuttle? No Shuttle? Shuttle? No Shuttle? Hard to decide.

You can go to the classroom either on walk or by shuttle.
Determine if it is possible not to be late. 

Constraint: max(Duration) <= 60
'''

import sys


# 1. TO GET THE INPUT

wait_time, bus_time, walk_time, left_time = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

bus_possible = True
if wait_time + bus_time > left_time:
    bus_possible = False

walk_possible = True
if walk_time > left_time:
    walk_possible = False

if bus_possible:
    if walk_possible:
        print("~.~")
    else:
        print("Shuttle")
else:
    if walk_possible:
        print("Walk")
    else:
        print("T.T")