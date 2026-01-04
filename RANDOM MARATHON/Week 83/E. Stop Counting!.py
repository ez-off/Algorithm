'''
E. Stop Counting!

A dealer reveals N cards in order, and keeps track of the sum of the values.
At some point, you can call "Stop!" at most once.
Then, the dealer continues displaying cards in order but does not include them in the running sums.
At some point after "Stop!", you can call "Start!" at most once.
Then, the dealer includes subsequent cards in the totals.
Determine the best average value of the counted cards.
'''

import sys


# 1. TO GET THE INPUT

card_count = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))


# 2. PREFIX SUM AND SUFFIX SUM

prefix_sum = [0 for idx in range(card_count)]
for idx in range(card_count):
    if idx == 0:
        prefix_sum[idx] = cards[idx]
    else:
        prefix_sum[idx] = prefix_sum[idx-1] + cards[idx]

suffix_sum = [0 for idx in range(card_count)]
for idx in range(1, card_count + 1):
    if idx == 1:
        suffix_sum[-idx] = cards[-idx]
    else:
        suffix_sum[-idx] = suffix_sum[-idx+1] + cards[-idx]


# 3. TO SOLVE THE PROBLEM
# To only look at prefix sum and suffix sum is sufficient.
# It is always possible to reduce the answer to either of them.

ans = 0
for idx in range(card_count):
    ans = max(ans, prefix_sum[idx] / (idx + 1))
    ans = max(ans, suffix_sum[-idx-1] / (idx + 1))
print(ans)