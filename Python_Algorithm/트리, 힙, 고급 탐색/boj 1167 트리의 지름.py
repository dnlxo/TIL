import sys
from collections import deque
import heapq

sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())

graph = [[] for n in range(N+1)]
# graph[i] = [node, cost] i에서 node로 가는 비용 : cost

for n in range(N) :
    edges = list(map(int, sys.stdin.readline().split()))
    edges_ = edges[1:-1]
    for i in range(len(edges_)) :
        if i % 2 == 0 :
            graph[edges[0]].append((edges_[i], edges_[i+1]))
            
INF = 9999999

def ds(start) :
    check = [False]*(N+1)
    heap = []
    heapq.heappush(heap, (0, start)) # (비용, 노드) 순서로 푸쉬

    table = [INF]*(N+1) # start 에서 table[i] 까지 거리
    table[start] = 0

    while heap :
        c, n = heapq.heappop(heap)
        if check[n] == True :
            continue
        
        for node_cost in graph[n] :
            node, cost = node_cost
            if c + cost < table[node] :
                table[node] = c + cost
                heapq.heappush(heap, (c + cost, node))   
        check[n] = True

    far_dist = 0
    far_node = 0
    for n in range(N+1) :
        if table[n] == INF :
            continue
        else :
            if far_dist < table[n] :
                far_node = n
                far_dist = table[n]
    return far_node, far_dist

fn, fd = ds(1)

print(ds(fn)[1])
