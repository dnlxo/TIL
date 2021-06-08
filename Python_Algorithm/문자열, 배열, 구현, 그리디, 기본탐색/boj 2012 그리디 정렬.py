import sys

N = int(sys.stdin.readline())

rank = []

for n in range(N) :
    rank.append(int(sys.stdin.readline()))

rank.sort()

compare = list(range(1,len(rank)+1))

angry = 0

for i in range(len(rank)) :
    angry += abs(compare[i] - rank[i])

print(angry)
