import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())

mat = [[0 for i in range(M)] for j in range(N)]

for k in range(K) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(y1, y2) :
        for j in range(x1, x2) :
            mat[i][j] = 1

def dfs(i,j) :
    global answer
    answer += 1
    check[i][j] = True
    for k in range(4) :
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < N and 0 <= ny < M :
            if mat[nx][ny] == 0 and not check[nx][ny] :
                dfs(nx,ny)

def bfs(ii,jj) :
    global answer
    need_visit = deque()
    need_visit.append((ii,jj))
    while need_visit :
        i, j = need_visit.popleft()
        check[i][j] = True
        answer += 1
        for k in range(4) :
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < M :
                if mat[nx][ny] == 0 and not check[nx][ny] :
                    need_visit.append((nx,ny))
                    check[nx][ny] = True


    
answers = []
block = 0
check = [[False for i in range(M)] for j in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N) :
    for j in range(M) :
        if mat[i][j] == 0 and not check[i][j] :
            answer = 0
            bfs(i,j)
            block += 1
            answers.append(answer)


    
print(block)
print(*sorted(answers))
