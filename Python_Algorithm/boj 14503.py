import sys
sys.setrecursionlimit(10000000)

N, M = map(int, sys.stdin.readline().split())

r, c, v = map(int, sys.stdin.readline().split())

mat = []
for n in range(N) :
    mat.append(list(map(int, sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
#북동남서 0123

def rotate(v) :
    if v == 0 :
        return 3
    else :
        return v-1

answer = 0
knt = 0

while True :
    
    if mat[r][c] == 0 :
        answer += 1
        mat[r][c] = 'c'
    
    if knt == 4 :
        knt = 0
        cnt = 0
        for k in range(4) :
           if mat[r+dx[k]][c+dy[k]] == 1 or mat[r+dx[k]][c+dy[k]] == 'c' :
               cnt += 1
               
        if cnt == 4 :
            if mat[r+dx[rotate(rotate(v))]][c+dy[rotate(rotate(v))]] == 1 :
                break
            else :
                r = r+dx[rotate(rotate(v))]
                c = c+dy[rotate(rotate(v))]
                
    if mat[r+dx[rotate(v)]][c+dy[rotate(v)]] == 0 :
        r = r+dx[rotate(v)]
        c = c+dy[rotate(v)]
        v = rotate(v)
        knt = 0
        continue
    
    elif mat[r+dx[rotate(v)]][c+dy[rotate(v)]] == 1 or mat[r+dx[rotate(v)]][c+dy[rotate(v)]] == 'c' :
        v = rotate(v)
        knt += 1
        continue
    
    

    
        
    

    
    
print(answer)
                                                                                                         
