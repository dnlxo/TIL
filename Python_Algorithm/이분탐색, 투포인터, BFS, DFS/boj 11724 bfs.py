import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

graph = [[] for n in range(N+1)]

for m in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
num = []

def bfs(start) :
    global num
    global cnt
    check = [False]*(N+1)
    need_visit = deque([start])
    check[start] = True
    num.append(start)
    while need_visit :
        i = need_visit.popleft()
        for node in graph[i] :
            if not check[node] :
                need_visit.append(node)
                check[node] = True
                num.append(node)
    cnt += 1

for n in range(1, N+1) :
    if n not in num : 
        bfs(n)

print(cnt)
