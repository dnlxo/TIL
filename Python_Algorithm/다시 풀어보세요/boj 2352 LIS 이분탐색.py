n = int(input())
port = list(map(int, input().split()))

# 1번 시간복잡도 N^2 통과 못함
'''
dp = [0]
port = [0] + port

for i in range(1,n+1) :
    max_idx = 0
    for j in range(len(dp)) :
        if port[j] < port[i] :
            if dp[j] > dp[max_idx] :
                max_idx = j

    dp.append(dp[max_idx]+1)

print(max(dp))
'''
# 2번 시간복잡도 NlogN

dp = [0]

low = 0

for i in range(n) :
    low = 0
    high = len(dp) - 1
    while low <= high :
        mid = (low + high) // 2
        if dp[mid] < port[i] :
            low = mid + 1
        else :
            high = mid - 1
    if low == len(dp) :
        dp.append(port[i])
    else :
        dp[low] = port[i]

print(len(dp) - 1)
    
