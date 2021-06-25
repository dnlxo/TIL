# boj 2110 이분탐색 밍밍..

import sys
N, C = map(int, sys.stdin.readline().split())
home = []

for n in range(N) :
    home.append(int(sys.stdin.readline()))

home.sort()

ans = 0

start = 1
end = home[-1] - home[0]

while start <= end : 
    mid = (start + end) // 2
    cnt = 1
    s_idx = 0
    i = 1
    while i < len(home) :
        if home[i] - home[s_idx] >= mid :
            s_idx = i
            cnt += 1
            i = s_idx + 1
        else :
            i += 1
    if cnt >= C :
        start = mid + 1
        ans = mid
    else :
        end = mid - 1
        
print(ans)
