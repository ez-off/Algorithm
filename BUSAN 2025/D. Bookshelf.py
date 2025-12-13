'''
D. Bookshelf

There is a bookshelf of length L holding N books.
You can perform the following operation any number of times:

(1) Choose one book on the shelf and take it out.
(2) Then, insert the book into any existing empty interval on the shelf whose length is larger than the width of the book.

You want to put K-th book at location P.
Determine if it is possible.

Constraint: N <= 100,000
'''

import sys


# 1. TO GET THE INPUT

book_count, shelf_length = map(int, sys.stdin.readline().split())

book_start = list(map(int, sys.stdin.readline().split()))
book_length = list(map(int, sys.stdin.readline().split()))

target_book, target_loc = map(int, sys.stdin.readline().split())
target_book -= 1


# 2. TO SOLVE THE PROBLEM
# The relative order of books larger than empty_length must be kept.
# The relative order of other books can be changed as you want.

empty_length = shelf_length - sum(book_length)

if book_length[target_book] <= empty_length:

    now_loc = 0
    
    for idx in range(book_count):
        if book_length[idx] > empty_length and idx != target_book:
            if now_loc <= target_loc:
                if now_loc + book_length[idx] <= target_loc:
                    now_loc += book_length[idx]
                else:
                    now_loc = target_loc + book_length[target_book] + book_length[idx]
            else:
                now_loc += book_length[idx]
    
    if now_loc <= shelf_length and target_loc + book_length[target_book] <= shelf_length:
        print("YES")
    else:
        print("NO")
    
else:
    
    left_length = 0
    right_length = 0
    
    for idx in range(book_count):
        if book_length[idx] > empty_length and idx != target_book:
            if idx < target_book:
                left_length += book_length[idx]
            else:
                right_length += book_length[idx]
    
    if left_length <= target_loc and target_loc + book_length[target_book] + right_length <= shelf_length:
        print("YES")
    else:
        print("NO")