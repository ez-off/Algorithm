'''
A. Yes or Yes

There is a string S only consisting of "Y" and "N".
You can repeatedly apply the following operation on S:

- Choose any two adjacent characters and replace them with logical OR.

Determine if it is possible to reduce S to a single character without ever combining two "Y"s.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    word = sys.stdin.readline().strip()
    
    
    # 2. TO SOLVE THE PROBLEM
    # Without combining two "Y"s, you can only delete "N" in an operation.
    
    if word.count("Y") < 2:
        print("YES")
    else:
        print("NO")