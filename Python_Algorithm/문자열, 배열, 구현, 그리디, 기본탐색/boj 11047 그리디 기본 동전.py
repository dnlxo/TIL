import sys
N, K = map(int, sys.stdin.readline().split())
coin = []
for n in range(N) :
    coin.append(int(sys.stdin.readline()))

cnt = 0
coin.sort(reverse = True)

for i in range(N) :
    if coin[i] <= K :
        cnt += (K // coin[i])
        K = K % coin[i]
    else : continue
    if K == 0 :
        break
    
print(cnt)
