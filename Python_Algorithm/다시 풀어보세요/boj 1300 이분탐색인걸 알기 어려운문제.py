N = int(input())
k = int(input())

low =  1
high = N**2

answer = 0

while low <= high :
    mid = (low + high) // 2
    cnt = 0
    for i in range(1, N+1) :
        cnt += min((mid // i), N)
        
    if cnt >= k :
        high = mid - 1
        answer = mid
    else :
        low = mid + 1
        
        
print(answer)
