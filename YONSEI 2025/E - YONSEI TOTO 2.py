'''
E. YONSEI TOTO 2

There are N classes.
You have S points and can use at most M points for each betting.
If you bet X points for class I, the probability of acceptance equals min(X / A[I], 1).
You can get satisfaction of B[I] if you are accepted in class I.
Make a bet so that the expectation value of satisfaction becomes the maximum.

Input : N <= 100000, M <= 1000
'''

import sys


# 1. TO GET THE INPUT

class_count, max_point, total_point = map(int, sys.stdin.readline().split())

popularity = list(map(int, sys.stdin.readline().split()))
score = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# It can be proved that the greedy approach based on B[i] / A[i] works.

arr = []
for idx in range(class_count):
    arr.append((score[idx], popularity[idx], idx))
arr.sort(key = lambda x : -(x[0] / x[1]))

ans = [0 for idx in range(class_count)]

for score, popularity, idx in arr:
    # There is no need to bet over A[I].
    max_bet = min(popularity, max_point)
    if max_bet <= total_point:
        ans[idx] = max_bet
        total_point -= max_bet
    else:
        ans[idx] = total_point
        break

print(" ".join(map(str, ans)))