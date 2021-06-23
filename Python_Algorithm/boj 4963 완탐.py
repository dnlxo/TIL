import sys
sys.setrecursionlimit(100000)
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]

def dfs(i, j) :
    global mat
    global check
    global dx
    global dy
    if check[i][j] :
        return
    check[i][j] = True
    for k in range(8) :
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < N and 0 <= ny < M :
            if mat[nx][ny] == 1 :
                dfs(nx,ny)
                
while True :
    try :
        M, N = map(int, sys.stdin.readline().split())
        if M == 0 and N == 0 :
            break
        mat = []
        check = [[False for i in range(M)] for j in range(N)]
        for n in range(N) :
            mat.append(list(map(int, sys.stdin.readline().split())))

        location_1 = []
        
        for i in range(N) :
            for j in range(M) :
                if mat[i][j] == 1 :
                    location_1.append((i,j))

        answer = 0
        
        for v in location_1 :
            i, j = v
            if not check[i][j] :
                dfs(i,j)
                answer += 1
        
        print(answer)
                    
        
    except :
        break
