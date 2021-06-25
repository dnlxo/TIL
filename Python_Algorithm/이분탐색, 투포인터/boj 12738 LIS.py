import sys
N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [-1000000001]

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
