'''
B. Korea After Yonsei

Determine if 'yonsei' comes faster than 'korea' in input.

Input : N <= 100
'''

import sys


# 1. TO GET THE INPUT

team_count = int(sys.stdin.readline())

teams = []
for team in range(team_count):
    name = sys.stdin.readline().strip()
    teams.append(name)


# 2. TO SOLVE THE PROBLEM

if teams.index("yonsei") < teams.index("korea"):
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")