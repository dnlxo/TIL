# boj 2606 바이러스 bfs

import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = {}
for n in range(1,N+1) :
    graph[n] = []
    
for m in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start_node) :
    need_visit = [start_node]
    visited = []
    while need_visit :
        v = need_visit.pop(0)
        if v in visited :
            pass
        else :
            visited.append(v)
            need_visit.extend(graph[v])
    return visited

print(len(bfs(graph, 1))-1)


