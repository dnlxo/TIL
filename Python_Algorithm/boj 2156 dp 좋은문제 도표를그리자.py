import sys

N = int(sys.stdin.readline())

wine = [None]
for n in range(N) :
    wine.append(int(sys.stdin.readline()))


dp = [0]*(N+1)

answer = []

answer.append(wine[1])
    
dp[1] = (wine[1], wine[1])
if N >= 2 :
    dp[2] = (wine[2], wine[1]+wine[2])
    answer.append(max(dp[2]))



for i in range(3, N+1) :
    dp[i] = (max(answer[:-1]) + wine[i],
             dp[i-1][0] + wine[i])
    
    answer.append(max(dp[i]))

print(max(answer))
