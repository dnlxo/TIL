import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())

mat = []

for n in range(N) :
    mat.append(list(map(int, sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i, j) :
    global mat
    global check
    global dx
    global dy
    if check[i][j] :
        return
    check[i][j] = True
    for k in range(4) :
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < N and 0 <= ny < N :
            if check[nx][ny] == False :
                dfs(nx,ny)
                
highest = []
for m in mat : 
    highest.append(max(m))
highest = max(highest)

answers = []

for h in range(highest+1) :
    check = [[False for i in range(N)] for j in range(N)]
    ground = []
    for i in range(N) :
        for j in range(N) :
            if mat[i][j] <= h :
                check[i][j] = True
            else :
                ground.append((i,j))

    answer = 0
    for v in ground :
        i, j = v
        if not check[i][j] :
            dfs(i,j)
            answer += 1

    answers.append(answer)

print(max(answers))
    
