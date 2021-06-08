import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = {}
for n in range(1,N+1) :
    graph[n] = []
for m in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for n in range(1,N+1) :
    graph[n].sort()
    
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
def dfs(graph, start_node) :
    need_visit = [start_node]
    visited = []
    while need_visit :
        v = need_visit.pop(0)
        if v in visited :
            pass
        else :
            visited.append(v)
            need_visit = graph[v] + need_visit
    return visited

print(*dfs(graph,V), sep=' ')
print(*bfs(graph,V), sep=' ')

