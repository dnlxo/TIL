dp = [0]

def upper_bound(data, target) :
    low = 0
    high = len(data)
    while low < high :
        mid = (low + high) // 2

        if data[mid] <= target :
            low = mid + 1
        else :
            high = mid
    return low
        
N = int(input())
seq = []
for n in range(N) :
    seq.append(int(input()))

for s in seq :
    if dp[-1] < s :
        dp.append(s)
    else :
        dp[upper_bound(dp, s)] = s


    
print(N - len(dp) + 1)
