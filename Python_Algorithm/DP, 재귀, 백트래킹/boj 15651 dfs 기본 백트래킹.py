N, M = map(int, input().split())
nums = list(range(1,N+1))
answer = []

def dfs(n) :
    if n == M :
        print(*answer)
        return
    for i in range(N) :
        answer.append(nums[i])
        dfs(n+1)
        answer.pop()

dfs(0)
