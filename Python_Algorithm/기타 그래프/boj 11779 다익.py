import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
path = [0]*(N+1)
graph = [[] for n in range(N+1)]

for m in range(M) :
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

start, end = map(int, sys.stdin.readline().split())
INF = 999999999

table = [INF]*(N+1)
check = [False]*(N+1)

table[start] = 0
heap = []
heapq.heappush(heap, (0, start))
while heap :
    weight, edge = heapq.heappop(heap)
    if check[edge] == True :
        continue
    for go in graph[edge] :
        e, w = go
        cost = weight + w
        if cost < table[e] :
            table[e] = cost
            heapq.heappush(heap, (cost, e))
            path[e] = edge
    check[edge] = True

print(table[end])
answer_path = []
def dfs(end) :
    if end == start :
        answer_path.append(start)
        return
    answer_path.append(end)
    dfs(path[end])
    
dfs(end)
answer_path.reverse()
print(len(answer_path))
print(*answer_path)
