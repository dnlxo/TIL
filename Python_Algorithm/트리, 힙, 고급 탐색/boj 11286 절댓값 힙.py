import heapq
import sys
N = int(sys.stdin.readline())
heap = []
for n in range(N) :
    num = int(sys.stdin.readline())
    if num == 0 :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
    else :
        heapq.heappush(heap, (abs(num), num))
