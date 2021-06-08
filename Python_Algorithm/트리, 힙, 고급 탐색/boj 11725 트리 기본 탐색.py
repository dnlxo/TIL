import sys
from collections import deque

N = int(sys.stdin.readline())
tree = {}
for n in range(1, N+1) :
    tree[n] = []

check = [False]*(N+1)
check[1] = True

parent = [0]*(N+1)

for n in range(N-1) :
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

need_visit = deque([])
need_visit.append(1)
    
while need_visit :
    i = need_visit.popleft()
    check[i] = True
    for j in tree[i] :
        if not check[j] :
            parent[j] = i
            need_visit.append(j)

for i in range(2,N+1) :
    print(parent[i])
    
