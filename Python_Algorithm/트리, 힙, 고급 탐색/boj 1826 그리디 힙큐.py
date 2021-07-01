import sys
import heapq
from collections import deque

N = int(sys.stdin.readline())

station = []
for n in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    station.append((a,b))

home, cur_gas = map(int, sys.stdin.readline().split())

station.sort()
cnt = 0
answer = 0
go = []
station = deque(station)
breaking = False

while cur_gas < home :
    
    while station :
        dist, gas = station.popleft()
        if dist <= cur_gas :
            heapq.heappush(go, -gas)
        else :
            station.appendleft((dist, gas))
            break
    
    if go :
        a = heapq.heappop(go)
        answer += 1
        cur_gas += -a
    else :
        breaking = True
        break

if breaking :
    print(-1)
else :
    print(answer)
