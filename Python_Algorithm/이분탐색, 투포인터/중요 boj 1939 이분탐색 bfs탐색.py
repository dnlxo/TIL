# boj 1939 이분탐색 그래프탐색
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dic = [[] for n in range(N+1)]
for m in range(M) :
    x, y, k = map(int, sys.stdin.readline().split())
    dic[x].append((y,k))
    dic[y].append((x,k))

s_node, e_node = map(int, sys.stdin.readline().split())

def bfs(weight) :
    que = deque([s_node])
    visited = [False for i in range(N+1)]
    visited[s_node] = True
    while que :
        go = que.popleft()
        # 갈 수 있는 곳 체크 후 큐에 넣기
        for island, w in dic[go] :
            if w >= weight and visited[island] == False :
                que.append(island)
                visited[island] = True
    return visited[e_node]

start = 1
end = 1000000000
ans = 0

while start <= end :
    mid = (start + end) // 2
    if bfs(mid) :
        start = mid + 1
        ans = mid
    else :
        end = mid - 1
print(ans)                
            
    
    
