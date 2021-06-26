N, K = map(int, input().split())
from collections import deque

check = [False]*100001

que = deque([(N,0)])
answer = []

while True :
    location, time = que.popleft()
    if location == K :
        answer.append((location, time))
        for _ in que :
            l, t = _
            if t > time :
                break
            if l == K and t == time :
                answer.append(_)
        break
    
    check[location] = True

    if location - 1 >= 0 :
        if not check[location-1] :
            que.append((location-1, time+1))
    if location + 1 <= 100000 :
        if not check[location+1] :
            que.append((location+1, time+1))
    if location*2 <= 100000 :
        if not check[location*2] :
            que.append((location*2, time+1))

print(answer[0][1])
print(len(answer))
    
