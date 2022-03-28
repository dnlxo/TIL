import sys
from collections import deque

N = int(sys.stdin.readline())

time = [0]*(N+1)
pre = [0]*(N+1)
connect = [[] for n in range(N+1)]
need_visit = deque([])
wholetime = [0]*(N+1)

for n in range(1, N+1) :
    task = list(map(int, sys.stdin.readline().split()))
    time[n] = task[0]
    pre[n] = task[1]
    for p in task[2:] :
        connect[p].append(n)

for n in range(1, N+1) :
    if pre[n] == 0 :
        need_visit.append(n)
        wholetime[n] = time[n]

while need_visit :
    done = need_visit.popleft()
    for d in connect[done] :
        pre[d] -= 1
        if pre[d] == 0 :
            need_visit.append(d)
        wholetime[d] = max(wholetime[done] + time[d], wholetime[d])

