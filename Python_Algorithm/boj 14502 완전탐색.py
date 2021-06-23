import sys
import copy
N, M = map(int, sys.stdin.readline().split())

mat = []

for n in range(N) :
    mat.append(list(map(int, sys.stdin.readline().split())))

location_0 = []
location_2 = []

for i in range(N) :
    for j in range(M) :
        if mat[i][j] == 0 :
            location_0.append((i,j))
        elif mat[i][j] == 2 :
            location_2.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(v) :
    i, j = v
    global temp
    global check
    global dx
    global dy
    if check[i][j] :
        return
    check[i][j] = True
    temp[i][j] = 2
    for k in range(4) :
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < N and 0 <= ny < M :
            if temp[nx][ny] == 0 :
                dfs((nx,ny))
    
ans = []

for i in range(len(location_0)) :
    for j in range(i+1, len(location_0)) :
        for k in range(j+1, len(location_0)) :
            temp = copy.deepcopy(mat)
            check = [[False for f in range(M)] for ff in range(N)]
            a, b = location_0[i]
            aa, bb = location_0[j]
            aaa, bbb = location_0[k]
            temp[a][b] = 1
            temp[aa][bb] = 1
            temp[aaa][bbb] = 1
            # spread the virus
            for v in location_2 :
                dfs(v)

            answer = 0
            for _i in range(N) :
                for _j in range(M) :
                    if temp[_i][_j] == 0 :
                        answer += 1
            ans.append(answer)

print(max(ans))
