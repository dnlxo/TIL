import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for n in range(N+1)]
for m in range(M) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

start, end = map(int, sys.stdin.readline().split())

INF = 9999999999

check = [False]*(N+1)
table = [INF]*(N+1)
table[start] = 0

heap = []
heapq.heappush(heap, (0, start)) # 비용, 노드 순서

while heap :
    w, e = heapq.heappop(heap) # weight, edge

    if check[e] == True :
        continue

    for i in graph[e] :
        edge, weight = i
        
        cost = w + weight

        if cost < table[edge] :
            table[edge] = cost
            heapq.heappush(heap, (cost, edge))

    check[e] = True

print(table[end])
