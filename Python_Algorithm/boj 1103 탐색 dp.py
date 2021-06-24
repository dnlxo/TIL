import sys
sys.setrecursionlimit(100000)
mat = []
N, M = map(int, sys.stdin.readline().split())
for n in range(N) :
    mat.append(list(sys.stdin.readline().rstrip()))

check = [[False for i in range(M)] for j in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
temp= False
dp = [[0]*M for i in range(N)]

def dfs(i,j,cnt) :
    global dx, dy
    global mat
    global ans
    global temp
    if mat[i][j] == 'H' :
        return
    ans = max(ans, cnt)
    check[i][j] = True
    for k in range(4) :
        nx = i + dx[k]*int(mat[i][j])
        ny = j + dy[k]*int(mat[i][j])
        if 0 <= nx < N and 0 <= ny < M and dp[nx][ny] <= cnt :
            if check[nx][ny] == False :
                dp[nx][ny] = cnt + 1
                dfs(nx,ny,cnt+1)
            else :
                print(-1)
                exit()

            check[nx][ny] = False

dfs(0,0,0)

print(ans+1)
