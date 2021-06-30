import sys
from collections import deque

N = int(sys.stdin.readline())

mat = [[0 for i in range(N)] for j in range(N)]

K = int(sys.stdin.readline())

apples = []
for k in range(K) :
    i, j = map(int, sys.stdin.readline().split())
    apples.append((i-1,j-1))
    mat[i-1][j-1] = 1
    

L = int(sys.stdin.readline())

directions = [0]*10001
for l in range(L) :
    s, v = sys.stdin.readline().split()
    s = int(s)
    directions[s] = v

def rotate(k, v) :
    if v == 'D' :
        k += 1
        if k == 4 :
            k = 0
            
        return k
    
    if v == 'L' :
        k -= 1
        if k == -1 :
            k = 3
            
        return k

dx = [-1,0,1,0]
dy = [0,1,0,-1]
k = 1 #0123 북동남서
r, c = 0, 0 #뱀의 위치
mat[r][c] = 2

snake = deque([])

time = 0
while True :
    mat[r][c] = 2
    snake.append((r,c))

    time += 1
    nr = r + dx[k]
    nc = c + dy[k]
    if 0 <= nr < N and 0 <= nc < N :
        if mat[nr][nc] == 1 :
            if directions[time] != 0 :
                k = rotate(k, directions[time])
            r, c = nr, nc
            
        elif mat[nr][nc] == 0 :
            i, j = snake.popleft()
            mat[i][j] = 0
            if directions[time] != 0 :
                k = rotate(k, directions[time])
            r, c = nr, nc
            
        elif mat[nr][nc] == 2 :
            break
            
    else :
        break
    
print(time)
