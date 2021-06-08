import sys
import heapq
N, K = map(int, sys.stdin.readline().split())
jewels = []
for n in range(N) :
    M, V = map(int, sys.stdin.readline().split())
    jewels.append((M,V))

jewels.sort()

answer = 0
bags = []
temp = []
for k in range(K) :
    bags.append(int(sys.stdin.readline()))
    
bags.sort()
cnt = 0
# --------------여기까지 힙 쓸필요가 없다....
# 보석 처음부터 끝까지 한번만 돌면됨!!!! 계속 첨부터 끝까지 돌필요 x
# 중간에 멈췄으면 중간부터 다시시작하면됨 정렬해놨으니까 >> cnt
for bag in bags :
    
    while cnt < N and bag >= jewels[cnt][0] :
        heapq.heappush(temp, -jewels[cnt][1])
        cnt += 1
        
    if temp :
        answer += -(heapq.heappop(temp))
    
print(answer)
