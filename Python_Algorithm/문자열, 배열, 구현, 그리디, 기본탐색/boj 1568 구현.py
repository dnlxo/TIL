# boj 1568 걍 구현

N = int(input())

cnt = 1
ans = 0
while N > 0 :
    if N >= cnt :
        N -= cnt
        cnt += 1
        ans += 1
    else :
        cnt = 1
print(ans)
