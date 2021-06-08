import heapq
import sys
N = int(sys.stdin.readline())
heap = []
for n in range(N) :
    heapq.heappush(heap, int(sys.stdin.readline()))
answer = 0
while len(heap) > 1 :
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    answer += a+b
print(answer)
