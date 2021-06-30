import sys
sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split())

mat = []

for n in range(N) :
    mat.append(list(map(int, sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melt() :
    global mat
    global location_1
    melted = []
    for l in range(len(location_1)) :
        i, j = location_1[l]
        cnt = 0
        for k in range(4) :
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M :
                if mat[nx][ny] == 'O' :
                    cnt += 1
        if cnt >= 2 :
            melted.append((i,j))
            

    for m in melted :
        i, j = m
        mat[i][j] = 'O'
        location_1.remove(m)

def air_outside(i,j) :
    global check
    global mat
    mat[i][j] = 'O'
    check[i][j] = True
    for k in range(4) :
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not check[nx][ny] :
            if mat[nx][ny] != 1 :
                air_outside(nx,ny)

location_1 = []

for i in range(N) :
    for j in range(M) :
        if mat[i][j] == 1 :
            location_1.append((i,j))



cnt = 0
while location_1 :
    check = [[False for m in range(M)] for n in range(N)]
    air_outside(0,0)
    melt()
    cnt += 1

print(cnt)
