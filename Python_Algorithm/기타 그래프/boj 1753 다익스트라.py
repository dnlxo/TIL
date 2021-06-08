import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph =[[] for v in range(V+1)]

for e in range(E) :
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

heap = []
heapq.heappush(heap,(0, start)) # (가중치, 노드) 순서
INF = 9999999
check = [False]*(V+1)

table = [INF]*(V+1) # start에서 table[i] 로 가는 거리
table[start] = 0

while heap :
    w, e = heapq.heappop(heap)
    
    if check[e] == True :
        continue
    
    for i in graph[e] :
        node, weight = i
        
        cost = w + weight
        if cost < table[node] :
            table[node] = cost
            heapq.heappush(heap, (cost, node))
        
    check[e] = True
    
for i in table[1:] :
    if i == INF :
        print('INF')
    else :
        print(i)
