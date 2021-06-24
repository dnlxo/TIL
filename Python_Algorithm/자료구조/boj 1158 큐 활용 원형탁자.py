N, K = map(int, input().split())

from collections import deque

que = deque(list(range(1,N+1)))

answer = []

while que :
    for k in range(K) :
        if k == K-1 :
            answer.append(que.popleft())
        else :
            que.append(que.popleft())

print('<', end = '')
print(*answer, sep= ', ', end = '')
print('>')
