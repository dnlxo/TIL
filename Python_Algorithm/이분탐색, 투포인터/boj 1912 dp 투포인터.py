import sys

N = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))

a, b = 0, 0

cur_sum = seq[0]
dp = []
dp.append(seq[0])

while b < N :

    if cur_sum <= 0 :
        b += 1
        if b >= N :
            break
        a = b
        cur_sum = seq[a]
        dp.append(cur_sum)

    else :
        while cur_sum > 0 :
            b += 1
            if b >= N :
                break
            cur_sum += seq[b]
            dp.append(cur_sum)

print(max(dp))
