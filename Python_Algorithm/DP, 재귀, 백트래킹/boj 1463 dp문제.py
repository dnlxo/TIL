import sys
sys.setrecursionlimit(1000000)

X = int(sys.stdin.readline())


dp = [0]*(X+1) # dp[i] : i가 1이 되기 위한 연산의 횟수

# 재귀 함수
def make_1(x) :
    if x == 1 :
        return 0
    if dp[x] != 0 :
        return dp[x]
    else :
        if x%6 == 0 :
            dp[x] = min(make_1(x//3), make_1(x//2), make_1(x-1)) + 1
            return dp[x]
        elif x%3 == 0 and x%2 != 0 :
            dp[x] = min(make_1(x//3), make_1(x-1)) + 1
            return dp[x]
        elif x%3 != 0 and x%2 == 0 :
            dp[x] = min(make_1(x//2), make_1(x-1)) + 1
            return dp[x]
        else :
            dp[x] = make_1(x-1) + 1
            return dp[x]
        

# 바텀업 풀이

make_1 = [0]*(10**6 + 1) # make_1[i] : i가 1이 되기 위한 연산의 횟수

make_1[1] = 0
make_1[2] = 1
make_1[3] = 1

for x in range(4, X+1) :
    if x%6 == 0 :
        make_1[x] = min(make_1[x//3], make_1[x//2], make_1[x-1]) + 1
        
    elif x%3 == 0 and x%2 != 0 :
        make_1[x] = min(make_1[x//3], make_1[x-1]) + 1

    elif x%3 != 0 and x%2 == 0 :
        make_1[x] = min(make_1[x//2], make_1[x-1]) + 1
        
    else :
        make_1[x] = make_1[x-1] + 1

print(make_1[X])
        


