# boj 7576 토마토

import sys
from collections import deque
class customEx(BaseException) : pass

M, N = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#상 하 좌 우
ans = 0
def bfs(start_node_list) :
    global box
    global ans
    n_visit = deque()
    n_visit.extend(start_node_list)
    visited = set()
    while n_visit :
        (i, j) = n_visit.popleft()
        if (i, j) not in visited : 
            visited.add((i,j))
            for k in range(4) :
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M :
                    if box[nx][ny] == 0 :
                        n_visit.append((nx,ny))
                        box[nx][ny] = box[i][j] + 1
    ans = box[i][j] - 1

starter = []
for i in range(N) :
    for j in range(M) :
        if box[i][j] == 1 :
            starter.append((i,j))
try :
    for i in box :
        if 0 in i :
            break
    else :
        print(0)
        raise customEx

    bfs(starter)

    for i in box :
        if 0 in i :
            print(-1)
            raise customEx
    else :
        print(ans)

except customEx :
    pass
