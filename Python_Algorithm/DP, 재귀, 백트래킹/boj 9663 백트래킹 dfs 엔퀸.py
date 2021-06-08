# boj 9663 n퀸 백트래킹

# row = [0,1,2,3] 이라 하면 4x4 체스판에
# 0행0열 1행1열 2행2열 3행3열에 퀸 배치한 것
import sys

def check(x) : 
    for i in range(x) : # x행 i열에 놔도 될까요?
        if row[x] == row[i] :
            return False # 같은 열이라 안되
        if abs(row[x] - row[i]) == x - i : 
            return False # 대각선이라 안대 (가로 세로 길이 같음)
    return True # 놔두대

def dfs(x) :
    global answer
    if x == N :
        answer += 1 # 체스판 완성될 때 마다 1 더해주기
    else :
        for i in range(N) :
            row[x] = i # 일단 놔버리기
            if check(x) : # 근데 놔도 되나 체크해보기
                dfs(x+1) # 놔도 되면 다음행 놓은채로 다음행 ㄱㄱ
                
N = int(sys.stdin.readline())

row = [0] * N
answer = 0
dfs(0)

print(answer)
