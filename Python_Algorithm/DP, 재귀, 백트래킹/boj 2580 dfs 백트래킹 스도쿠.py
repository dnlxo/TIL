import sys
sudoku = []
for i in range(9) :
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    
blank = []
for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            blank.append((i,j))

ans = list(range(1,10))

def check(i, j) :
    global sudoku
    cnt = 0
    for k in range(9) :
        if sudoku[i][j] == sudoku[i][k] :
            cnt += 1
    if cnt >= 2 :
        cnt = 0
        return False
    cnt = 0
    for k in range(9) :
        if sudoku[i][j] == sudoku[k][j] :
            cnt += 1
    if cnt >= 2 :
        cnt = 0
        return False
    cnt = 0
    for k in range(3) :
        for kk in range(3) :
            if sudoku[i][j] == sudoku[(i//3)*3 + k][(j//3)*3 + kk] :
                cnt += 1
    if cnt >= 2 :
        cnt = 0
        return False
    cnt = 0
    return True

def dfs(b) :
    
    if b == len(blank) :
        for sudo in sudoku :
            print(*sudo)
        exit()
        return
    (i, j) = blank[b]
    for num in ans :
        sudoku[i][j] = num
        if check(i, j) :
            dfs(b+1)
        else:
            sudoku[i][j] = 0
            continue
    sudoku[i][j] = 0
    return
    
dfs(0)
