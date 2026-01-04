'''
C. Rigged Rock-Scissors-Paper (Small)

Two players - A and B - play rock-scissors-paper for multiple rounds.
Except for the first round, player A will throw the same hand player B threw at last round.
However, if player A draws right after the round he/she won, audiences will know the game is rigged.
Given player B's plan, determine the number of its sub-sequences that allow players to finish the game without audiences knowing the game is rigged.
'''

import sys


# 2. ROCK-SCISSORS-PAPER FUNCTION

def rock_scissors_paper(playerA, playerB):
    
    key = playerA + playerB
    
    if key == "RS" or key == "SP" or key == "PR":
        return "Win"
    elif key == "RR" or key == "SS" or key == "PP":
        return "Draw"
    else:
        return "Lose"


# 1. TO GET THE INPUT

playerA_first = sys.stdin.readline().strip()
playerB_plan = sys.stdin.readline().strip()

plan_length = len(playerB_plan)


# 3. TO SOLVE THE PROBLEM - BRUTE-FORCE

ans = 0

for case in range(1, 1 << plan_length):
    
    # Bit-masking
    
    playerB = []
    for idx in range(plan_length):
        if case & (1 << idx):
            playerB.append(playerB_plan[idx])
    
    playerA_win = False
    possible = True
    for idx in range(len(playerB)):
        if idx == 0:
            result = rock_scissors_paper(playerA_first, playerB[idx])
        else:
            result = rock_scissors_paper(playerB[idx-1], playerB[idx])
        if result == "Win":
            playerA_win = True
        else:
            if result == "Draw":
                if playerA_win:
                    possible = False
                    break
            playerA_win = False
    
    if possible:
        ans += 1

print(ans)