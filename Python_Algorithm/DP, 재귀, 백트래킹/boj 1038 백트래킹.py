N = int(input())

answer = 1

def dfs(n) :
    global answer
    a = list(map(int, str(n)))
    if len(set(a)) != len(a) :
        return
    if a == sorted(a, reverse = True) :
        answer += 1
        return
n = 1
while answer < N :
    dfs(n)
    n += 1

print(n)

# 시간초과 

