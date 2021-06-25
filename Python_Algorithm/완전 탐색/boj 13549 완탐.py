N, K = map(int, input().split())
import heapq

check = [False]*100001

que = []
heapq.heappush(que, (0,N))

while True :
    time, location = heapq.heappop(que)
    if location == K :
        print(time)
        break
    
    check[location] = True

    if location - 1 >= 0 :
        if not check[location-1] :
            heapq.heappush(que, (time+1,location-1))
    if location + 1 <= 100000 :
        if not check[location+1] :
            heapq.heappush(que, (time+1,location+1))
    if location*2 <= 100000 :
        if not check[location*2] :
            heapq.heappush(que, (time,location*2))
    
