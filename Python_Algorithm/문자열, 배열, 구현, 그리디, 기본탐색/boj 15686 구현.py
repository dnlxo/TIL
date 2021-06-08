import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = []

for n in range(N) :
    city.append(list(map(int, sys.stdin.readline().split())))

homes = []
chicken = []

for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            homes.append((i,j))
        elif city[i][j] == 2 :
            chicken.append((i,j))

stay_chicken = list(combinations(chicken, M))
answer = []
for chickens in stay_chicken :
    dist = 0
    for home in homes :
        temp = []
        for ch in chickens :
            temp.append((abs(home[0] - ch[0]) + abs(home[1] - ch[1])))
        dist += min(temp)
    answer.append(dist)

print(min(answer))
