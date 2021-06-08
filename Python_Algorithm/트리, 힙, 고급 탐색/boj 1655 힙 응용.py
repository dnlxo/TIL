import heapq
import sys

heap = []
HEAP = []

N = int(sys.stdin.readline())
for n in range(N) :
    a = int(sys.stdin.readline())

    if len(heap) == 0 and len(HEAP) == 0 :
        heapq.heappush(heap, (-a,a))
    elif HEAP == [] and a < heap[0][1] :
        heapq.heappush(HEAP, heapq.heappop(heap)[1])
        heapq.heappush(heap, (-a,a))
    elif HEAP == [] and a > heap[0][1] :
        heapq.heappush(HEAP, a)

    elif len(heap) == len(HEAP) :
        if a > HEAP[0] :
            temp = heapq.heappop(HEAP)
            heapq.heappush(heap, (-temp, temp))
            heapq.heappush(HEAP, a)
        else :
            heapq.heappush(heap, (-a,a))
    else :
        if a < heap[0][1] :
            temp = heapq.heappop(heap)
            heapq.heappush(HEAP, temp[1])
            heapq.heappush(heap, (-a,a))
        else :
            heapq.heappush(HEAP, a)
    
    print(heap[0][1])
