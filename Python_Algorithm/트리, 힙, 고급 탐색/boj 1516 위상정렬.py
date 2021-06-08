import sys
from collections import deque

N = int(sys.stdin.readline())

pre = [0]*(N+1)
build = [[] for n in range(N+1)]
time = [0]*(N+1)
wholetime = [0]*(N+1)
visited = [False]*(N+1)

for n in range(1, N+1) :
    data = list(map(int, sys.stdin.readline().split()))
    for i in data[1:-1] :
        build[i].append(n)
        pre[n] += 1
    time[n] = data[0]
    
need_visit = deque()
for i in range(1, N+1) :
    if pre[i] == 0 :
        need_visit.append(i)

while need_visit :
    idx = need_visit.popleft()
    visited[idx] = True
    wholetime[idx] += time[idx]
    for b in build[idx] :
        pre[b] -= 1
        if pre[b] == 0 and not visited[b] :
            need_visit.append(b)
        wholetime[b] = max(wholetime[b], wholetime[idx])

for w in wholetime[1:] : print(w)

