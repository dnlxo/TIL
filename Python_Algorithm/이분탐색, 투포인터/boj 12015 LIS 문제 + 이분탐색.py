
import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [0]

for i in range(N) :
    low = 0
    high = len(dp) - 1
    while low <= high :
        mid = (low + high) // 2
        if dp[mid] < seq[i] :
            low = mid + 1
        else :
            high = mid - 1

    if low == len(dp) :
        dp.append(seq[i])
    else : 
        dp[low] = seq[i]

print(len(dp)-1)
        

#아래 코드는
#시간복잡도 n^2 인 대신 그 부분 수열을 알아낼 수 있다.


import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
seq = [0] + seq

dp = [0]

for i in range(1, N+1) :
    max_idx = 0
    for j in range(len(dp)) : # 돌면서 seq[i] 보다 값이 작고 dp값이 최대인 곳의 인덱스 찾기
        if seq[j] < seq[i] :
            if dp[j] >= dp[max_idx] :
                max_idx = j
        
    dp.append(dp[max_idx] + 1)

print(max(dp))


