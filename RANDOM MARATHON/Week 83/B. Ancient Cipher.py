'''
B. Ancient Cipher

There are two types of encryption.
Substitution cipher changes all occurrences of each letter to some other letter.
Permutation cipher applies some permutation to change the order of the letters of the message.
You have a code which is first encrypted using substitution cipher and then permutation cipher.
Determine if a given code can be the result of encrypting the given message.
'''

import sys


# 1. TO GET THE INPUT

code = sys.stdin.readline().strip()
text = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM
# If distributions are the same, it is possible that the code could be the result of encrypting the message.

code_count = [0 for alphabet in range(26)]
text_count = [0 for alphabet in range(26)]

for idx in range(len(code)):
    
    code_char = code[idx]
    code_count[ord(code_char) - 65] += 1
    
    text_char = text[idx]
    text_count[ord(text_char) - 65] += 1

code_count.sort()
text_count.sort()

if code_count == text_count:
    print("YES")
else:
    print("NO")