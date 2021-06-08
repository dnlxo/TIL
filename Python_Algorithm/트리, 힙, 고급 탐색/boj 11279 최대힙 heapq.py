import heapq
import sys

heap = []

N = int(sys.stdin.readline())
for n in range(N) :
    a = int(sys.stdin.readline())

    if a == 0 :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
    else :
        heapq.heappush(heap, (-a,a))

