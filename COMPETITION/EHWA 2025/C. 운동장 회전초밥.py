'''
C. Track Conveyor Belt Sushi

A track consists of followings:

(1) Two trapezoids of which the length of upper edge equals D.
(2) Two sectors of which diameter equals R and central angle equals θ. 
(3) The width of track equals W.

Three women - X, Y, and Z from the innermost lane - rotates the field N laps.
Determine the difference of average velocity between X and Z, and Y and Z.

Constraint: N <= 20, R <= 1000, D <= 3000, θ <= 180, W <= 300
'''


import sys
from math import cos, pi, radians


# 2. A FUNCTION TO GET AVERAGE VELOCITY

def velocity(dist_from_center):
    
    one_lap_dist =  2 * D + 4 * dist_from_center * cos(radians(THETA / 2)) + dist_from_center * pi * THETA / 90
    velocity = one_lap_dist * turn_count / time

    return velocity


# 1. TO GET THE INPUT

turn_count, time = map(int, sys.stdin.readline().split())
R, D, THETA, W = map(int, sys.stdin.readline().split())
W /= 100


# 3. TO SOLVE THE PROBLEM

print(velocity(R - W / 2) - velocity(R - 5 * W / 2))
print(velocity(R - W / 2) - velocity(R - 3 * W / 2))
