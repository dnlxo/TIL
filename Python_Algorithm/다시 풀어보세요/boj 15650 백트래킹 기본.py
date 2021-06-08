N, M = map(int,input().split())
answer = [0]
check = [False]*N
nums = list(range(1,N+1))

def dfs(n) :
    if n == M :
        print(*answer[1:])
        return

    for i in range(N) :
        if not check[i] and nums[i] > answer[-1]:
            answer.append(nums[i])

            check[i] = True

            dfs(n+1)

            check[i] = False
            answer.pop()
    

dfs(0)
