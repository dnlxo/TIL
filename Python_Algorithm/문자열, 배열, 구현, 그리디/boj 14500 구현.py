import sys
sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split())

mat = []
for n in range(N) :
    mat.append(list(map(int, sys.stdin.readline().split())))

answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit = [[False for m in range(M)] for n in range(N)]
check = [[False for m in range(M)] for n in range(N)]

def dfs(i,j,cnt,length) :
    global answer
    global check
    
    if length == 1 :
        if visit[i][j] :
            return
        else :
            visit[i][j] = True
    
    if length == 4 :
        visit[i][j] = True
        answer = max(answer, cnt)
        return
    
    check[i][j] = True
    
    for k in range(4) :
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < N and 0 <= ny < M :
            if not check[nx][ny] :
                dfs(nx,ny,cnt+mat[nx][ny],length+1)
                check[nx][ny] = False

    check[i][j] = False


for i in range(N) :
    for j in range(M) :
        if not visit[i][j] :
            dfs(i,j,mat[i][j],1)



for i in range(N) :
    for j in range(M) :
        ux, dx, uy, dy = i-1, i+1, j+1, j-1
        uux, ddx, uuy, ddy = i-2, i+2, j+2, j-2
        #ㅜ
        if 0 <= uuy < M and 0 <= dx < N :
            answer = max(answer, mat[i][j] + mat[i][uy] + mat[i][uuy] + mat[dx][uy])
        #ㅏ
        if 0 <= ddx < N and 0 <= uy < M :
            answer = max(answer, mat[i][j] + mat[dx][j] + mat[ddx][j] + mat[dx][uy])
        #ㅗ
        if 0 <= uuy < M :
            answer = max(answer, mat[i][j] + mat[i][uy] + mat[i][uuy] + mat[ux][uy])
        #ㅓ
        if 0 <= ddx < N and 0 <= dy < M :
            answer = max(answer, mat[i][j] + mat[dx][j] + mat[ddx][j] + mat[dx][dy])
        

print(answer)
