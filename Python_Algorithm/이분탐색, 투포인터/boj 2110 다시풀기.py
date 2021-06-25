import sys
N, C = map(int, sys.stdin.readline().split())
home = []
for n in range(N) :
    home.append(int(sys.stdin.readline()))

home.sort()

def setup(alist) :
    low = 1
    high = max(home) - min(home)
    answer = 0
    while low <= high :
        mid = (low + high) // 2
        cnt = 1
        s_idx = 0
        i = 1
        while i <= len(home) - 1 :
            if home[i] - home[s_idx] >= mid :
                cnt += 1
                s_idx = i
                i = s_idx + 1
            else :
                i += 1
                
        if cnt >= C :
            answer = mid
            low = mid + 1
        else :
            high = mid - 1
            
    return answer

print(setup(home))
