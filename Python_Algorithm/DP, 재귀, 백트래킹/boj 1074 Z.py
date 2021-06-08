# boj 1074 재귀
import sys

N, r, c = map(int,sys.stdin.readline().split())
ans = 0
M = N
def z(i, j, N) :
    global ans
    if N < M : # 시간초과 안나게 하는 부분 @@@
        if not i <= r < i + 2**N and not j <= c < j + 2**N :
            ans += (2**N)**2
            return
    if N == 1 :
        if (i, j) == (r, c) :
            print(ans)
            return
        ans += 1
        if (i, j+1) == (r, c) :
            print(ans)
            return
        ans += 1
        if (i+1, j) == (r, c) :
            print(ans)
            return
        ans += 1
        if (i+1, j+1) == (r, c) :
            print(ans)
            return
        ans += 1
        return
    z(i, j, N-1)
    z(i, j + 2**(N-1), N-1)
    z(i + 2**(N-1), j, N-1)
    z(i + 2**(N-1), j + 2**(N-1), N-1)
    
z(0,0,N)
