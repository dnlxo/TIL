import sys
N, M = map(int, sys.stdin.readline().split())
from collections import deque

island = [[] for i in range(N+1)]
for m in range(M) :
    A, B, C = map(int, sys.stdin.readline().split())
    island[A].append((B,C))
    island[B].append((A,C))

start, destination = map(int, sys.stdin.readline().split())

def bfs(start_node) :
    need_visit = deque([start_node])
    visited = set()
    visited.add(start_node)
    while need_visit :
        node = need_visit.popleft()
        for nodes in island[node] :
            if nodes[0] not in visited :
                if nodes[1] >= mid :
                    need_visit.append(nodes[0])
                    visited.add(nodes[0])
                    if nodes[0] == destination :
                        return True
    return False

low = 1
high = 1000000000
answer = 0

while low <= high :
    mid = (low + high) // 2
    if bfs(start) :
        answer = mid
        low = mid + 1
    else :
        high = mid - 1

print(answer)


                    
