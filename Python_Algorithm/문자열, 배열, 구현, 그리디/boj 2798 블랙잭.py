# boj 2798 블랙잭

import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
ans = []
for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            cnt = A[i] + A[j] + A[k]
            if cnt <= M :
                ans.append(cnt)
print(max(ans))            
