'''
D. Yonsei University

An English word is called 'good' if it satisfies the following conditions:

Consider two consecutive characters (A[i], A[i+1]) in the word.
Let X be the count of pairs where A[i] < A[i+1] in lexicographical order, and Y be the count of pairs where A[i] > A[i+1].

(1) Each character is used at most once.
(2) |X - Y| <= 1

Given a prefix of length 5, construct the shortest good word possible.

Input : N <= 5
'''

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
word = sys.stdin.readline().strip()


# 2. TO CALCULATE INITIAL X AND Y + CHECK IF THE LETTER IS USED

ascent = 0
descent = 0

used = [0 for alphabet in range(26)]

for idx in range(length - 1):
    used[ord(word[idx]) - 65] = 1
    if word[idx] < word[idx+1]:
        ascent += 1
    else:
        descent += 1

used[ord(word[-1]) - 65] = 1


# 3. TO SOLVE THE PROBLEM

if abs(ascent - descent) <= 1:
    
    pass

else:

    if ascent < descent:
        
        for alphabet in range(ord(word[-1]) - 65, 26):
            if used[alphabet] == 0:
                word += chr(alphabet + 65)
                used[alphabet] = 1
                ascent += 1
                if ascent + 1 == descent:
                    break
        
        if ascent + 1 != descent:
            descent += 2
            for alphabet in range(26):
                if used[alphabet] == 0:
                    word += chr(alphabet + 65)
                    used[alphabet] = 1
                    ascent += 1
                    if ascent + 1 == descent:
                        break
        
    else:
        
        for alphabet in range(ord(word[-1]) - 65 - 1, -1, -1):
            if used[alphabet] == 0:
                word += chr(alphabet + 65)
                used[alphabet] = 1
                descent += 1
                if descent + 1 == ascent:
                    break
        
        if descent + 1 != ascent:
            ascent += 2
            for alphabet in range(25, -1, -1):
                if used[alphabet] == 0:
                    word += chr(alphabet + 65)
                    used[alphabet] = 1
                    descent += 1
                    if descent + 1 == ascent:
                        break

print(len(word))
print(word)