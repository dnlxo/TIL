#boj 2178 미로탐색 bfs

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
maze = []
for n in range(N) :
    p = list(map(int, list(str(sys.stdin.readline())[:-1])))
    maze.append(p)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] #상 우 하 좌 순으로 체크

check = [[False for m in range(M)] for n in range(N)]

n_visit = deque()
n_visit.append((0,0))
while n_visit :
    (i,j) = n_visit.popleft()
    check[i][j] = True #방문했다고 체크
    for k in range(4) :
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < N and 0 <= ny < M :
            if check[nx][ny] == False and maze[nx][ny] == 1 :
                #방문되어있지 않고, 이동할 수 있으면
                n_visit.append((nx, ny))
                maze[nx][ny] = maze[i][j] + 1
                #즉 상우하좌 체크 후 큐에 넣고

print(maze[-1][-1])
