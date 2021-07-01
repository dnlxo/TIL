import sys
from collections import deque

def bfs(s,e) :
    dist = [0]*(N+1)
    check = [False]*(N+1)
    que = deque()
    que.append(s)
    while que :
        q = que.popleft()
        check[q] = True
        for node, cost in tree[q] :
            if not check[node] :
                que.append(node)
                dist[node] += dist[q]+cost
    print(dist[e])

N, M = map(int, sys.stdin.readline().split())

tree = [[] for n in range(N+1)]

for n in range(N-1) :
    i, j, w = map(int, sys.stdin.readline().split())
    tree[i].append((j,w))
    tree[j].append((i,w))

for m in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    bfs(i,j)
