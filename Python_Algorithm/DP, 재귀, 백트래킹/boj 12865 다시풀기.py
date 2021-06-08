import sys
N, K = map(int, sys.stdin.readline().split())
W = []
V = []
for n in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    W.append(a)
    V.append(b)

dp = [[False for i in range(K+1)] for j in range(N+1)]
      
def dfs(w, n) :
    global dp
    if n == N :
        return 0
    if dp[n][w] != False :
        return dp[n][w]

    n1 = 0
    if w + W[n] <= K :
        n1 = V[n] + dfs(w + W[n], n+1)

    n2 = 0 + dfs(w, n+1)

    dp[n][w] = max(n1, n2)
    return dp[n][w]

print(dfs(0, 0))

        
