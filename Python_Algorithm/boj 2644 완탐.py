N = int(input())

from collections import deque

man1, man2 = map(int, input().split())

n = int(input())

fam = [[] for __ in range(N+1)]
check = [False for i in range(N+1)]

for _ in range(n) :
    a, b = map(int, input().split())
    fam[a].append(b)
    fam[b].append(a)

answer = 0
def bfs(ii, jj, ccnt) :
    global answer
    que = deque()
    que.append((ii,ccnt))
    check[ii] = True
    while que :
        (i, cnt) = que.popleft()
        if i == jj :
            answer = cnt
            break
        for ni in fam[i] :
            if not check[ni] :
                que.append((ni, cnt+1))
                check[ni] = True

bfs(man1, man2, 0)
if answer == 0 :
    print(-1)
else :
    print(answer)
