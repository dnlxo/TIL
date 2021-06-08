import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
maze = []
for r in range(R) :
    maze.append(list(sys.stdin.readline().rstrip()))

water = deque([])
temp = deque([])
temp2 = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
wcheck = [[False for i in range(C)] for j in range(R)]
check = [[False for i in range(C)] for j in range(R)]

for i in range(R) :
    for j in range(C) :
        if maze[i][j] == '*' :
            water.append((i, j))
        elif maze[i][j] == 'S' :
            start = (i, j)
            maze[i][j] = 1

def bfs(start_node) :
    global water
    global temp
    global temp2
    need_visit = deque([start_node])

    while need_visit :
        while need_visit :
            (i, j) = need_visit.popleft()
            check[i][j] = True
            if str(maze[i][j]) in 'X*' :
                continue
            for k in range(4) :
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < R and 0 <= ny < C :
                    if maze[nx][ny] == 'D' :
                        print(maze[i][j])
                        exit()
                    elif maze[nx][ny] == '.' and not check[nx][ny] :
                        maze[nx][ny] = maze[i][j] + 1
                        temp2.append((nx,ny))
                        check[nx][ny] = True
        need_visit.extend(temp2)
        temp2.clear()
                    
                    
                
        while water :
            (ii, jj) = water.popleft()
            wcheck[ii][jj] = True
            for k in range(4) :
                nnx, nny = ii + dx[k], jj + dy[k]
                if 0 <= nnx < R and 0 <= nny < C :
                    if str(maze[nnx][nny]) not in 'DX' and not wcheck[nnx][nny] :
                        maze[nnx][nny] = '*'
                        temp.append((nnx, nny))
                        wcheck[nnx][nny] = True
        water.extend(temp)
        temp.clear()
        
        
bfs(start)

print('KAKTUS')
