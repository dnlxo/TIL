N, M = map(int, input().split())
from collections import deque

seq = list(map(int, input().split()))
seq.sort()

check = [False]*(10001)

temp = deque()

def dfs(cnt) :
    global temp
    
    if cnt == M :
        print(*temp)
        return
        
    for i in seq :
        if not check[i] :
            check[i] = True
            temp.append(i)
            dfs(cnt+1)
            check[i] = False
            temp.pop()

dfs(0)
