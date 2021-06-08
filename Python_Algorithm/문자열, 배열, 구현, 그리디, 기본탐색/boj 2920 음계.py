# boj 2920 배열 구현

import sys

A = list(map(int, sys.stdin.readline().split()))

if sorted(A) == A :
    print('ascending')
elif sorted(A, reverse = True) == A :
    print('descending')
else :
    print('mixed')
