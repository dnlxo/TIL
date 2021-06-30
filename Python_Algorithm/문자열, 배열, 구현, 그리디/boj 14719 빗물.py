# boj 14719 빗물

import sys

H, W = map(int, sys.stdin.readline().split())

world = [[] for i in range(H)]

block = list(map(int, sys.stdin.readline().split()))

for i in block :
    for j in range(H - i) :
        world[j].append(0)
    for k in range(H - i, H) :
        world[k].append(1)

cnt = 0

for A in world :
    idx1 = []
    for i in range(len(A)) :
        if A[i] == 1 :
            idx1.append(i)
    if len(idx1) >= 2 :
        cnt += idx1[-1] - idx1[0] - len(idx1) + 1

print(cnt)
