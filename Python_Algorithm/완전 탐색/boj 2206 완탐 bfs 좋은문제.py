import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
mat = []
for n in range(N) :
    mat.append(list(map(int, sys.stdin.readline().rstrip())))

answer = [[[False, False] for _ in range(M)] for __ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer[0][0][0] = 1
    
que = deque()
que.append((0,0,0))

def bfs() :
    while que :
        
        i, j, w = que.popleft()
        
        for k in range(4) :
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < M :
                if mat[nx][ny] == 0 and not answer[nx][ny][w] :
                    answer[nx][ny][w] = answer[i][j][w] + 1
                    que.append((nx,ny,w))
                    
                elif mat[nx][ny] == 1 and w == 0 and not answer[nx][ny][1] :
                    answer[nx][ny][1] = answer[i][j][w] + 1
                    que.append((nx,ny,1))

bfs()

if min(answer[-1][-1]) == False :
    if not answer[-1][-1][0] and not answer[-1][-1][1] :
        print(-1)
    elif answer[-1][-1][0] :
        print(answer[-1][-1][0])
    elif answer[-1][-1][1] :
        print(answer[-1][-1][1])
        
else :
    print(min(answer[-1][-1]))
            
