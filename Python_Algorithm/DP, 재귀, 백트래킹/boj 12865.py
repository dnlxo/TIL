# 12865 평범한 배낭
'''
그리디로 풀면 ㄴㄴ
1. 무게가 작은 순으로 넣기,
2. 가치가 큰 순으로 넣기. 둘다 안댐
결국 모든 경우의 수를 다 해야댐
모든 물건 n개에 대하여 넣기 or 빼기
즉 2의 n승 개의 경우를 모두 해야함
memoization 하기
'''

import sys

N, K = map(int, sys.stdin.readline().split())
W = []
V = []
for n in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    W.append(a)
    V.append(b)

dp = [[False for i in range(K+1)] for j in range(N+1)]

def put_in(i, w) :
    global dp
    if i == N :
        return 0 #마지막 물건까지 확인 시 재귀종료
    
    if dp[i][w] != False :
        return dp[i][w]
    
    n1 = 0
    if w + W[i] <= K :
        n1 = V[i] + put_in(i + 1, w + W[i]) #i번째 물건 넣었으니 i번째 물건의 가치 추가 + 재귀

    n2 = 0 + put_in(i + 1, w) #i번째 물건을 안 넣음 현재 배낭무게 그대로 다음물건 재귀

    dp[i][w] = max(n1,n2) #put_in(i, w) 의 결과 dp에 저장하기
    return dp[i][w]

print(put_in(0, 0))
