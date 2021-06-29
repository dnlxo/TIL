# boj 2667 단지번호붙이기 bfs

import sys
from collections import deque
N = int(sys.stdin.readline())

maze = []
cnt = 0
ans = []
for n in range(N) :
    p = list(map(int, list(str(sys.stdin.readline()[:-1]))))
    maze.append(p)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] #상하좌우

def bfs(start_node) :
    global maze
    global cnt
    global ans
    n_visit = deque()
    n_visit.append(start_node)
    visited = set()
    while n_visit :
        (i,j) = n_visit.popleft()
        visited.add((i,j))
        maze[i][j] = 0
        for k in range(4) :
            nx, ny = i + dx[k], j +dy[k]
            if 0 <= nx < N and 0 <= ny < N :
                if maze[nx][ny] == 1 and (nx,ny) not in n_visit :
                    n_visit.append((nx,ny))

    cnt += 1
    ans.append(len(visited))

for p in range(N) :
    for q in range(N) :
        if maze[p][q] == 1 :
            bfs((p,q))

print(cnt)
for i in sorted(ans) : print(i)
        
    
