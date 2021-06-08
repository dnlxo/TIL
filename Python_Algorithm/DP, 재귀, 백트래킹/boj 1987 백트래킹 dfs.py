# boj 1987 알파벳 백트래킹 dfs

import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
maze = []
for r in range(R) :
    maze.append(sys.stdin.readline().rstrip())



dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 1

que = set()
que.add((0,0, maze[0][0]))

while que :
    (i, j, route) = que.pop()
    answer = max(answer, len(route))
    
    for k in range(4) :
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < R and 0 <= ny < C :
            if maze[nx][ny] not in route :
                que.add((nx, ny, route + maze[nx][ny]))
            
print(answer)
