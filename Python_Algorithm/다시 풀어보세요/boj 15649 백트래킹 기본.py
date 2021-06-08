import sys

N, M = map(int, sys.stdin.readline().split())

nums = list(range(1, N+1))
answer = []
check = [False]*N

def dfs(n) :
    if n == M :
        print(*answer)
        return

    for i in range(N) :
        if not check[i] :
            answer.append(nums[i])
            check[i] = True

            dfs(n+1)
        
            check[i] = False
            answer.pop()
            

dfs(0)
