from collections import deque

T = int(input())

dx = [-2,-1,-2,-1,2,1,2,1]
dy = [-1,-2,1,2,-1,-2,1,2]

def bfs(ii,jj) :
    global end
    que = deque()
    que.append((ii,jj))
    while que :
        i, j = que.popleft()
        check[i][j] = True
        if [i, j] == end :
            print(mat[i][j])
            break
        for k in range(8) :
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < N :
                if mat[nx][ny] == 0 and not check[nx][ny] :
                    mat[nx][ny] = mat[i][j] + 1
                    que.append((nx,ny))
                    check[nx][ny] = True
                    
for t in range(T) :
    N = int(input())
    mat = [[0 for i in range(N)] for j in range(N)]
    check = [[False for i in range(N)] for j in range(N)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    i, j = start 
    bfs(i,j)
    


