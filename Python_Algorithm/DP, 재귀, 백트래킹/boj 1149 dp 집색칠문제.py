N = int(input())

houses = []

for n in range(N) :
    houses.append(list(map(int, input().split())))

dp = [[0,0,0] for i in range(1001)]

dp[1] = houses[0]
for i in range(2, len(houses)+1) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i-1][2]

print(min(dp[len(houses)]))
